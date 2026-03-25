from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    household_id: Optional[str] = None



class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    household_id: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True  # important for Beanie    