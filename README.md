# DocsGenTray Platform

Production-ready monorepo for selling and licensing an offline Windows document generation app.

## Included services
- **Frontend**: Next.js App Router with SEO pages (220 generated long-tail pages).
- **Backend**: FastAPI API (auth, cabinet, admin, bot integration, licensing).
- **License crypto**: Ed25519 signing/verification for offline activation.
- **Telegram bot**: aiogram bot for license status and renew requests.
- **Infra**: Docker Compose stack with healthchecks and restart policies.

## Quick start
```bash
docker compose -f infrastructure/docker-compose.yml up --build
```

## Runtime checks
- Frontend: `http://localhost:3000`
- Backend docs: `http://localhost:8000/docs`
- Backend health: `http://localhost:8000/health`
- Backend readiness: `http://localhost:8000/ready`

## Security highlights
- Offline license validation via Ed25519.
- Private key only server-side (`/run/secrets`).
- JWT auth + Argon2 password hashing.
- Security headers middleware and admin guards.
