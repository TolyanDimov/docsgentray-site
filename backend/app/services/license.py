import json
from datetime import datetime, timedelta, timezone
from base64 import b64decode

try:
    from license_service.crypto import sign_activation_payload
except ModuleNotFoundError:
    from app.services.license_crypto import sign_activation_payload

TARIFF_DAYS = {'1m': 30, '3m': 90, '6m': 180, '12m': 365}


def decode_device_key(device_key: str) -> dict:
    raw = b64decode(device_key.encode('utf-8')).decode('utf-8')
    return json.loads(raw)


def generate_license(device_key: str, tariff: str) -> tuple[str, datetime]:
    payload = decode_device_key(device_key)
    expires_at = datetime.now(timezone.utc) + timedelta(days=TARIFF_DAYS.get(tariff, 30))
    license_payload = {
        'email': payload['email'],
        'phone': payload.get('phone'),
        'fingerprint': payload['fingerprint'],
        'tariff': tariff,
        'exp': expires_at.isoformat(),
    }
    return sign_activation_payload(license_payload), expires_at
