from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from slowapi import Limiter
from slowapi.util import get_remote_address
from app.core.db import Base, engine, get_db
from app.models.user import User
from app.models.license import License
from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse
from app.schemas.license import LicenseGenerateRequest, LicenseResponse
from app.services.security import hash_password, verify_password, create_access_token
from app.services.license import generate_license, decode_device_key
from app.api.deps import get_current_user, require_admin

app = FastAPI(title='DocsGenTray API', version='1.0.0')
limiter = Limiter(key_func=get_remote_address)
Base.metadata.create_all(bind=engine)


@app.get('/health')
def health() -> dict:
    return {'status': 'ok'}


@app.post('/auth/register', response_model=TokenResponse)
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(status_code=400, detail='Email already used')
    user = User(
        email=payload.email,
        hashed_password=hash_password(payload.password),
        phone=payload.phone,
        telegram=payload.telegram,
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
def me(user: User = Depends(get_current_user)):
    return {
        'email': user.email,
        'phone': user.phone,
        'telegram': user.telegram,
    }


@app.post('/licenses/generate', response_model=LicenseResponse)
def create_license(
    payload: LicenseGenerateRequest,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
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
def admin_users(db: Session = Depends(get_db), _: User = Depends(require_admin)):
    users = db.query(User).all()
    return [
        {
            'id': u.id,
            'email': u.email,
            'phone': u.phone,
            'telegram': u.telegram,
            'created_at': u.created_at,
        }
        for u in users
    ]


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
