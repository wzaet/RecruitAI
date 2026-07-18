from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class LanguageBase(BaseModel):
    name: str
    proficiency: str
    display_order: int = 0


class LanguageCreate(LanguageBase):
    pass


class LanguageUpdate(BaseModel):
    name: Optional[str] = None
    proficiency: Optional[str] = None
    display_order: Optional[int] = None


class LanguageResponse(LanguageBase):
    id: int
    resume_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)