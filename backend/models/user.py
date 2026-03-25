from beanie import Document
from pydantic import EmailStr, Field
from datetime import datetime, UTC
from typing import Optional


class User(Document):
    name: str
    email: EmailStr
    password: str
    household_id: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    class Settings:
        name = "users"