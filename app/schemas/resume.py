from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ResumeBase(BaseModel):
    title: str
    summary: Optional[str] = None
    current_position: Optional[str] = None
    current_company: Optional[str] = None
    years_of_experience: int = 0
    city: Optional[str] = None
    country: Optional[str] = None
    resume_file: Optional[str] = None
    is_public: bool = True


class ResumeCreate(ResumeBase):
    pass


class ResumeUpdate(BaseModel):
    title: Optional[str] = None
    summary: Optional[str] = None
    current_position: Optional[str] = None
    current_company: Optional[str] = None
    years_of_experience: Optional[int] = None
    city: Optional[str] = None
    country: Optional[str] = None
    resume_file: Optional[str] = None
    parsed: Optional[bool] = None
    is_public: Optional[bool] = None


class ResumeResponse(ResumeBase):
    id: int
    user_id: int
    parsed: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)