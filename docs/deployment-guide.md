# Deployment Guide

1. Generate Ed25519 keypair and mount into `/run/secrets`.
2. Configure environment variables for DB, Redis, JWT secrets and bot token.
3. Build and run compose stack:
   ```bash
   docker compose -f infrastructure/docker-compose.yml up --build
   ```
4. Put CDN and reverse proxy (TLS) in front of frontend/backend.
5. Enable backups, monitoring, and alerting.

## Required env variables
- `SECRET_KEY`
- `ADMIN_EMAIL`
- `BOT_API_TOKEN`
- `DATABASE_URL`
- `REDIS_URL`
