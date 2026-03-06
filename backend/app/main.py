import csv
import io
from datetime import datetime

import redis
from fastapi import FastAPI, Depends, HTTPException, Query, Header
from fastapi.responses import StreamingResponse
from openpyxl import Workbook
from sqlalchemy import text, or_
from sqlalchemy.orm import Session
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.api.deps import get_current_user, require_admin
from app.core.config import settings
from app.core.db import Base, engine, get_db
from app.models.license import License
from app.models.user import User
from app.schemas.admin import AdminUserUpdateRequest, AdminLicenseActionRequest, AdminBlockRequest
from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse
from app.schemas.license import LicenseGenerateRequest, LicenseResponse
from app.services.license import generate_license, decode_device_key
from app.services.security import hash_password, verify_password, create_access_token

app = FastAPI(title='DocsGenTray API', version='1.3.0')
limiter = Limiter(key_func=get_remote_address)
Base.metadata.create_all(bind=engine)


@app.middleware('http')
async def add_security_headers(request, call_next):
    response = await call_next(request)
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'"
    return response


def _license_status(license_row: License | None) -> str:
    if not license_row:
        return 'inactive'
    if license_row.is_blocked:
        return 'blocked'
    if license_row.expires_at < datetime.utcnow():
        return 'expired'
    return 'active'


def _get_user_license_row(db: Session, user_id: int) -> License | None:
    return db.query(License).filter(License.user_id == user_id).order_by(License.id.desc()).first()


@app.get('/health')
def health() -> dict:
    return {'status': 'ok', 'service': 'backend'}


@app.get('/ready')
def ready(db: Session = Depends(get_db)) -> dict:
    db.execute(text('SELECT 1'))
    redis.Redis.from_url(settings.redis_url).ping()
    return {'status': 'ready'}


@app.post('/auth/register', response_model=TokenResponse)
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=400, detail='Email already used')
    user = User(
        email=payload.email,
        hashed_password=hash_password(payload.password),
        phone=payload.phone,
        telegram=payload.telegram,
        is_admin=payload.email == settings.admin_email,
    )
    db.add(user)
    db.commit()
    return TokenResponse(access_token=create_access_token(user.email))


@app.post('/auth/login', response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=401, detail='Bad credentials')
    return TokenResponse(access_token=create_access_token(user.email))


@app.get('/me')
def me(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    license_row = _get_user_license_row(db, user.id)
    return {
        'email': user.email,
        'phone': user.phone,
        'telegram': user.telegram,
        'license': {
            'key': license_row.activation_key if license_row else None,
            'tariff': license_row.tariff if license_row else None,
            'expires_at': license_row.expires_at if license_row else None,
            'fingerprint': license_row.device_fingerprint if license_row else None,
            'status': _license_status(license_row),
        },
    }


@app.post('/licenses/generate', response_model=LicenseResponse)
def create_license(payload: LicenseGenerateRequest, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    license_key, expires_at = generate_license(payload.device_key, payload.tariff)
    decoded = decode_device_key(payload.device_key)
    record = License(
        user_id=user.id,
        device_fingerprint=decoded['fingerprint'],
        device_key_payload=payload.device_key,
        activation_key=license_key,
        tariff=payload.tariff,
        expires_at=expires_at,
    )
    db.add(record)
    db.commit()
    return LicenseResponse(license_key=license_key, tariff=payload.tariff, expires_at=expires_at)


@app.get('/admin/users')
def admin_users(
    db: Session = Depends(get_db),
    _: User = Depends(require_admin),
    q: str | None = Query(None),
    status: str | None = Query(None),
    page: int = Query(1, ge=1),
    per_page: int = Query(20, ge=1, le=100),
):
    query = db.query(User)
    if q:
        query = query.filter(or_(User.email.ilike(f'%{q}%'), User.phone.ilike(f'%{q}%'), User.telegram.ilike(f'%{q}%')))
    users = query.order_by(User.id.desc()).all()

    rows = []
    for user in users:
        lic = _get_user_license_row(db, user.id)
        row_status = _license_status(lic)
        if status and row_status != status:
            continue
        rows.append({
            'id': user.id,
            'email': user.email,
            'phone': user.phone,
            'telegram': user.telegram,
            'license_key': lic.activation_key if lic else None,
            'tariff': lic.tariff if lic else None,
            'activated_at': lic.activated_at if lic else None,
            'expires_at': lic.expires_at if lic else None,
            'device_fingerprint': lic.device_fingerprint if lic else None,
            'status': row_status,
            'created_at': user.created_at,
        })

    total = len(rows)
    start = (page - 1) * per_page
    end = start + per_page
    return {'items': rows[start:end], 'page': page, 'per_page': per_page, 'total': total}


@app.get('/admin/users/export.csv')
def admin_export_csv(db: Session = Depends(get_db), _: User = Depends(require_admin)):
    users = db.query(User).order_by(User.id.asc()).all()
    out = io.StringIO()
    writer = csv.writer(out)
    writer.writerow(['ID', 'Email', 'Phone', 'Telegram', 'Tariff', 'ExpiresAt', 'Status'])
    for user in users:
        lic = _get_user_license_row(db, user.id)
        writer.writerow([
            user.id,
            user.email,
            user.phone,
            user.telegram,
            lic.tariff if lic else '',
            lic.expires_at.isoformat() if lic and lic.expires_at else '',
            _license_status(lic),
        ])
    out.seek(0)
    return StreamingResponse(iter([out.getvalue()]), media_type='text/csv', headers={'Content-Disposition': 'attachment; filename=users.csv'})


@app.get('/admin/users/export.xlsx')
def admin_export_xlsx(db: Session = Depends(get_db), _: User = Depends(require_admin)):
    users = db.query(User).order_by(User.id.asc()).all()
    wb = Workbook()
    ws = wb.active
    ws.title = 'Users'
    ws.append(['ID', 'Email', 'Phone', 'Telegram', 'Tariff', 'ExpiresAt', 'Status'])
    for user in users:
        lic = _get_user_license_row(db, user.id)
        ws.append([
            user.id,
            user.email,
            user.phone,
            user.telegram,
            lic.tariff if lic else '',
            lic.expires_at.isoformat() if lic and lic.expires_at else '',
            _license_status(lic),
        ])

    stream = io.BytesIO()
    wb.save(stream)
    stream.seek(0)
    return StreamingResponse(
        stream,
        media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        headers={'Content-Disposition': 'attachment; filename=users.xlsx'},
    )


@app.patch('/admin/users/{user_id}')
def admin_update_user(user_id: int, payload: AdminUserUpdateRequest, db: Session = Depends(get_db), _: User = Depends(require_admin)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    if payload.phone is not None:
        user.phone = payload.phone
    if payload.telegram is not None:
        user.telegram = payload.telegram
    db.commit()
    return {'ok': True}


@app.post('/admin/users/{user_id}/renew')
def admin_renew_license(user_id: int, payload: AdminLicenseActionRequest, db: Session = Depends(get_db), _: User = Depends(require_admin)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    lic = _get_user_license_row(db, user.id)
    if not lic:
        raise HTTPException(status_code=404, detail='License not found')
    license_key, expires_at = generate_license(lic.device_key_payload, payload.tariff)
    lic.activation_key = license_key
    lic.tariff = payload.tariff
    lic.expires_at = expires_at
    lic.is_blocked = False
    db.commit()
    return {'ok': True, 'expires_at': expires_at, 'tariff': payload.tariff}


@app.post('/admin/users/{user_id}/regenerate-key')
def admin_regenerate_key(user_id: int, db: Session = Depends(get_db), _: User = Depends(require_admin)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    lic = _get_user_license_row(db, user.id)
    if not lic:
        raise HTTPException(status_code=404, detail='License not found')
    license_key, _ = generate_license(lic.device_key_payload, lic.tariff)
    lic.activation_key = license_key
    db.commit()
    return {'ok': True, 'license_key': license_key}


@app.post('/admin/users/{user_id}/block')
def admin_block_license(user_id: int, payload: AdminBlockRequest, db: Session = Depends(get_db), _: User = Depends(require_admin)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    lic = _get_user_license_row(db, user.id)
    if not lic:
        raise HTTPException(status_code=404, detail='License not found')
    lic.is_blocked = payload.blocked
    db.commit()
    return {'ok': True, 'status': _license_status(lic)}


@app.delete('/admin/users/{user_id}')
def admin_delete_user(user_id: int, db: Session = Depends(get_db), _: User = Depends(require_admin)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    db.query(License).filter(License.user_id == user.id).delete()
    db.delete(user)
    db.commit()
    return {'ok': True}


@app.get('/bot/license/{email}')
def bot_license_lookup(
    email: str,
    db: Session = Depends(get_db),
    x_bot_token: str | None = Header(default=None),
):
    if x_bot_token != settings.bot_api_token:
        raise HTTPException(status_code=401, detail='Invalid bot token')

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    lic = _get_user_license_row(db, user.id)
    return {
        'email': user.email,
        'tariff': lic.tariff if lic else None,
        'expires_at': lic.expires_at if lic else None,
        'status': _license_status(lic),
        'license_key': lic.activation_key if lic else None,
    }


@app.get('/seo/pages')
def seo_pages():
    occupations = [
        'lawyers', 'accountants', 'hr', 'sales', 'procurement', 'construction', 'medical', 'education',
        'finance', 'manufacturing', 'logistics', 'real-estate', 'consulting', 'insurance', 'banking',
        'government', 'retail', 'it', 'legal', 'auditors',
    ]
    intents = ['from-excel', 'contract-generator', 'invoice-generator', 'pdf-export', 'template-automation', 'mail-merge', 'offline']
    pages = []
    for occ in occupations:
        for intent in intents:
            slug = f'document-generator-{intent}-for-{occ}'
            pages.append({'slug': slug, 'title': f'Document generator {intent} for {occ}'})
    return {'total': len(pages), 'pages': pages}
