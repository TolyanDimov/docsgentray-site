# DocsGenTray Platform

Production-ready monorepo for selling and licensing an offline Windows document generation app.

## Stack
- Frontend: Next.js + TypeScript + Tailwind
- Backend: FastAPI + PostgreSQL + Redis + JWT
- License cryptography: Ed25519 signed offline-verifiable tokens
- Bot: Python + aiogram
- Infra: Docker, Docker Compose, GitHub Actions

## Repository Structure
- `frontend/` — marketing site, dashboard, admin UI, SEO pages
- `backend/` — API (auth, users, licensing, admin)
- `license-service/` — asymmetric crypto licensing core
- `telegram-bot/` — customer support and license status bot
- `infrastructure/` — docker/nginx/env templates
- `tests/` — backend and frontend tests
- `docs/` — architecture and deployment docs

## Quick start
```bash
docker compose -f infrastructure/docker-compose.yml up --build
```

Open:
- Frontend: http://localhost:3000
- Backend docs: http://localhost:8000/docs

## Security highlights
- Offline license validation via Ed25519 signatures
- JWT auth + password hashing (Argon2)
- API rate limiting via Redis
- Security headers + robots/sitemap/metadata

