from beanie import Document
from pydantic import Field
from datetime import datetime, UTC
from typing import List


def utc_now():
    return datetime.now(UTC)


class Household(Document):
    name: str
    members: List[str] = []  # list of user IDs

    created_at: datetime = Field(default_factory=utc_now)

    class Settings:
        name = "households"