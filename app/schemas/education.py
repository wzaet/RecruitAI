from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class EducationBase(BaseModel):
    institution_name: str
    degree: str
    field_of_study: Optional[str] = None
    location: Optional[str] = None
    start_date: date
    end_date: Optional[date] = None
    is_current: bool = False
    grade: Optional[str] = None
    description: Optional[str] = None
    display_order: int = 0


class EducationCreate(EducationBase):
    pass


class EducationUpdate(BaseModel):
    institution_name: Optional[str] = None
    degree: Optional[str] = None
    field_of_study: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    is_current: Optional[bool] = None
    grade: Optional[str] = None
    description: Optional[str] = None
    display_order: Optional[int] = None


class EducationResponse(EducationBase):
    id: int
    resume_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)