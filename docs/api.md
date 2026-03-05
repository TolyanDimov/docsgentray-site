# API Documentation

## Auth
- `POST /auth/register`
- `POST /auth/login`

## User cabinet
- `GET /me`
- `POST /licenses/generate`

## Admin panel
- `GET /admin/users?q=&status=&page=&per_page=`
- `GET /admin/users/export.csv`
- `GET /admin/users/export.xlsx`
- `PATCH /admin/users/{user_id}`
- `POST /admin/users/{user_id}/renew`
- `POST /admin/users/{user_id}/regenerate-key`
- `POST /admin/users/{user_id}/block`
- `DELETE /admin/users/{user_id}`

## Bot integration
- `GET /bot/license/{email}` with header `x-bot-token`

## SEO
- `GET /seo/pages`
