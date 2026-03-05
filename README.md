# DocsGenTray Platform

Production-ready monorepo for selling and licensing an offline Windows document generation app.

## What is included
- Marketing website (Next.js App Router, SSR pages, SEO engine with 220 long-tail pages).
- FastAPI backend with JWT auth, cabinet and admin APIs.
- Offline-safe license signing with Ed25519 asymmetric cryptography.
- Telegram bot for license status and renewal request intake.
- Dockerized infrastructure (frontend, backend, Postgres, Redis, bot).
- CI pipeline skeleton (tests/build/docker/security step).

## Stack
- Frontend: Next.js + TypeScript + Tailwind
- Backend: FastAPI + PostgreSQL + Redis + JWT
- License crypto: Ed25519 signed offline-verifiable tokens
- Bot: Python + aiogram
- Infra: Docker, Docker Compose, GitHub Actions

## Repository Structure
- `frontend/` — landing pages, SEO pages, cabinet/admin UI pages
- `backend/` — auth, licensing, admin, SEO APIs
- `license-service/` — cryptographic signing/verification core
- `telegram-bot/` — Telegram integration
- `infrastructure/` — compose and container wiring
- `tests/` — tests
- `docs/` — deployment + architecture + API docs

## Quick start
```bash
docker compose -f infrastructure/docker-compose.yml up --build
```

Open:
- Frontend: http://localhost:3000
- Backend OpenAPI: http://localhost:8000/docs

## Security highlights
- Offline license validation via Ed25519 signatures
- Private key stored server-side only (`/run/secrets`)
- JWT auth + Argon2 password hashing
- Admin-guarded operations for license lifecycle
