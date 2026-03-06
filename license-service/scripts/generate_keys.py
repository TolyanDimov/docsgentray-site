from pathlib import Path
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

out = Path('../keys').resolve()
out.mkdir(parents=True, exist_ok=True)
private_key = Ed25519PrivateKey.generate()
public_key = private_key.public_key()

(out / 'license_private.pem').write_bytes(
    private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
)
(out / 'license_public.pem').write_bytes(
    public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
)
print('Keys generated:', out)
