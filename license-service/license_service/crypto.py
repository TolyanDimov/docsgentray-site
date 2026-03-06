import base64
import json
import os
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from cryptography.hazmat.primitives import serialization

PRIVATE_KEY_PATH = os.getenv('LICENSE_PRIVATE_KEY_PATH', '/run/secrets/license_private.pem')
PUBLIC_KEY_PATH = os.getenv('LICENSE_PUBLIC_KEY_PATH', '/run/secrets/license_public.pem')


def _load_private_key() -> Ed25519PrivateKey:
    with open(PRIVATE_KEY_PATH, 'rb') as file:
        return serialization.load_pem_private_key(file.read(), password=None)


def _load_public_key() -> Ed25519PublicKey:
    with open(PUBLIC_KEY_PATH, 'rb') as file:
        return serialization.load_pem_public_key(file.read())


def create_device_key(fingerprint: str, email: str, phone: str | None = None) -> str:
    payload = {'fingerprint': fingerprint, 'email': email, 'phone': phone}
    return base64.b64encode(json.dumps(payload).encode('utf-8')).decode('utf-8')


def sign_activation_payload(payload: dict) -> str:
    private_key = _load_private_key()
    serialized = json.dumps(payload, sort_keys=True).encode('utf-8')
    signature = private_key.sign(serialized)
    token = {
        'payload': base64.b64encode(serialized).decode('utf-8'),
        'signature': base64.b64encode(signature).decode('utf-8'),
        'alg': 'Ed25519',
    }
    return base64.b64encode(json.dumps(token).encode('utf-8')).decode('utf-8')


def verify_activation_payload(token: str) -> dict:
    public_key = _load_public_key()
    unpacked = json.loads(base64.b64decode(token.encode('utf-8')).decode('utf-8'))
    payload = base64.b64decode(unpacked['payload'].encode('utf-8'))
    signature = base64.b64decode(unpacked['signature'].encode('utf-8'))
    public_key.verify(signature, payload)
    return json.loads(payload.decode('utf-8'))
