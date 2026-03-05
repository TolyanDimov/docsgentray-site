from datetime import datetime
from pydantic import BaseModel


class LicenseGenerateRequest(BaseModel):
    device_key: str
    tariff: str


class LicenseResponse(BaseModel):
    license_key: str
    tariff: str
    expires_at: datetime
