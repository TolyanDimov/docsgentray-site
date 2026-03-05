# Deployment Guide

1. Generate Ed25519 keypair and mount into `/run/secrets`.
2. Configure environment variables for DB, Redis, JWT secrets.
3. Build and run compose stack.
4. Put CDN and reverse proxy (TLS) in front of frontend/backend.
5. Enable backups, monitoring, and alerting.
