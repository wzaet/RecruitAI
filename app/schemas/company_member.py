from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class CompanyMemberBase(BaseModel):
    role: str = "RECRUITER"
    is_active: bool = True


class CompanyMemberCreate(CompanyMemberBase):
    company_id: int
    user_id: int


class CompanyMemberUpdate(BaseModel):
    role: Optional[str] = None
    is_active: Optional[bool] = None


class CompanyMemberResponse(CompanyMemberBase):
    id: int
    company_id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)