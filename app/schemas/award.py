from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class AwardBase(BaseModel):
    title: str
    issuer: Optional[str] = None
    award_date: Optional[date] = None
    description: Optional[str] = None
    award_url: Optional[str] = None
    display_order: int = 0


class AwardCreate(AwardBase):
    pass


class AwardUpdate(BaseModel):
    title: Optional[str] = None
    issuer: Optional[str] = None
    award_date: Optional[date] = None
    description: Optional[str] = None
    award_url: Optional[str] = None
    display_order: Optional[int] = None


class AwardResponse(AwardBase):
    id: int
    resume_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)