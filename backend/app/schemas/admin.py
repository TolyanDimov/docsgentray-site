from datetime import datetime
from pydantic import BaseModel


class AdminUserRow(BaseModel):
    id: int
    email: str
    phone: str | None = None
    telegram: str | None = None
    created_at: datetime
    license_key: str | None = None
    tariff: str | None = None
    activated_at: datetime | None = None
    expires_at: datetime | None = None
    status: str


class AdminUserUpdateRequest(BaseModel):
    phone: str | None = None
    telegram: str | None = None


class AdminLicenseActionRequest(BaseModel):
    tariff: str


class AdminBlockRequest(BaseModel):
    blocked: bool
