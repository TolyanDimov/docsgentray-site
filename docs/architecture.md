# Architecture for 1M users

CDN -> Next.js SSR -> API Gateway -> FastAPI services -> PostgreSQL + Redis.

## Scalability
- Horizontal scaling for frontend/backend stateless containers.
- Redis cache for rate limiting and hot read patterns.
- PostgreSQL with read replicas and partitioning strategy for licenses/events.
- Queue-based async processing for heavy operations and export jobs.

## Security
- Ed25519 asymmetric signing for activation keys.
- Private key only in server-side secret store (KMS/HSM compatible).
- Public key embedded in Windows desktop app for offline verification.
- JWT auth, Argon2 password hashing, admin role guard.
