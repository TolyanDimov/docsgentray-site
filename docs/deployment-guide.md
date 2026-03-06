# Deployment Guide

## 1) Secrets and keys
1. Generate Ed25519 keypair and mount into `/run/secrets` for backend container.
2. Set secure production values:
   - `SECRET_KEY`
   - `ADMIN_EMAIL`
   - `BOT_API_TOKEN`
   - `DATABASE_URL`
   - `REDIS_URL`

## 2) Build and run
```bash
docker compose -f infrastructure/docker-compose.yml up --build -d
```

## 3) Validate runtime health
- Backend liveness: `GET /health`
- Backend readiness (DB + Redis): `GET /ready`
- Frontend: `GET /`

## 4) Production recommendations
- Put CDN + reverse proxy (TLS) in front of frontend/backend.
- Use managed PostgreSQL and Redis with backups.
- Rotate secrets and private signing key regularly.
- Enable centralized logs, metrics and alerting.
