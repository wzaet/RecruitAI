from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ResumeLinkBase(BaseModel):
    platform: str
    url: str
    is_primary: bool = False
    display_order: int = 0


class ResumeLinkCreate(ResumeLinkBase):
    pass


class ResumeLinkUpdate(BaseModel):
    platform: Optional[str] = None
    url: Optional[str] = None
    is_primary: Optional[bool] = None
    display_order: Optional[int] = None


class ResumeLinkResponse(ResumeLinkBase):
    id: int
    resume_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)