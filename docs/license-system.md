# License System

1. Desktop app creates `device_key` (base64 JSON: fingerprint, email, phone).
2. User submits key in website cabinet.
3. Backend generates signed activation token (`Ed25519`).
4. Desktop app verifies signature offline with embedded public key.
