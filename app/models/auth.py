"""Auth response models."""

from datetime import timedelta
from typing import Optional
from pydantic import BaseModel
from app.config import settings


class AccessToken(BaseModel):
    """Access token details."""

    access_token: str
    access_token_expires: timedelta = settings.access_token_expire_minutes


class RefreshToken(AccessToken):
    """Access and refresh token details."""

    refresh_token: str
    refresh_token_expires: timedelta = settings.access_token_expire_minutes


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str]