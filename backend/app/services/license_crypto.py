import base64
import json
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

PRIVATE_KEY_PATH = os.getenv('LICENSE_PRIVATE_KEY_PATH', '/run/secrets/license_private.pem')


def sign_activation_payload(payload: dict) -> str:
    with open(PRIVATE_KEY_PATH, 'rb') as file:
        private_key = serialization.load_pem_private_key(file.read(), password=None)

    if not isinstance(private_key, Ed25519PrivateKey):
        raise ValueError('Unsupported private key type, expected Ed25519')

    serialized = json.dumps(payload, sort_keys=True).encode('utf-8')
    signature = private_key.sign(serialized)
    token = {
        'payload': base64.b64encode(serialized).decode('utf-8'),
        'signature': base64.b64encode(signature).decode('utf-8'),
        'alg': 'Ed25519',
    }
    return base64.b64encode(json.dumps(token).encode('utf-8')).decode('utf-8')
