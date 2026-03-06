from datetime import datetime
from sqlalchemy import String, DateTime, Integer, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.core.db import Base


class License(Base):
    __tablename__ = 'licenses'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), index=True)
    device_fingerprint: Mapped[str] = mapped_column(String(256), index=True)
    device_key_payload: Mapped[str] = mapped_column(String(2048))
    activation_key: Mapped[str] = mapped_column(String(4096), unique=True)
    tariff: Mapped[str] = mapped_column(String(32))
    activated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    expires_at: Mapped[datetime] = mapped_column(DateTime)
    is_blocked: Mapped[bool] = mapped_column(Boolean, default=False)
