from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ReferenceBase(BaseModel):
    full_name: str
    job_title: Optional[str] = None
    company: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    relationship_type: Optional[str] = None
    is_public: bool = False
    display_order: int = 0


class ReferenceCreate(ReferenceBase):
    pass


class ReferenceUpdate(BaseModel):
    full_name: Optional[str] = None
    job_title: Optional[str] = None
    company: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    relationship_type: Optional[str] = None
    is_public: Optional[bool] = None
    display_order: Optional[int] = None


class ReferenceResponse(ReferenceBase):
    id: int
    resume_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)