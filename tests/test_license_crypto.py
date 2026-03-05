import os
from pathlib import Path
import pytest

cryptography = pytest.importorskip('cryptography')
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization
from license_service.crypto import sign_activation_payload, verify_activation_payload


def write_keys(tmp_path: Path):
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()

    priv = tmp_path / 'private.pem'
    pub = tmp_path / 'public.pem'
    priv.write_bytes(private_key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8, serialization.NoEncryption()))
    pub.write_bytes(public_key.public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo))
    return priv, pub


def test_sign_verify_roundtrip(tmp_path):
    priv, pub = write_keys(tmp_path)
    os.environ['LICENSE_PRIVATE_KEY_PATH'] = str(priv)
    os.environ['LICENSE_PUBLIC_KEY_PATH'] = str(pub)
    payload = {'email': 'a@b.com', 'fingerprint': 'abc', 'tariff': '1m', 'exp': '2026-01-01'}
    token = sign_activation_payload(payload)
    decoded = verify_activation_payload(token)
    assert decoded['fingerprint'] == 'abc'
