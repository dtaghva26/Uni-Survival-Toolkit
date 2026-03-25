from pydantic import BaseModel
from typing import List, Optional

class HouseholdCreate(BaseModel):
    name: str
    members: Optional[List[str]] = None
from pydantic import BaseModel
from typing import List
from datetime import datetime

class HouseholdResponse(BaseModel):
    id: str
    name: str
    members: List[str]
    created_at: datetime

    class Config:
        from_attributes = True    