from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ResumeSkillBase(BaseModel):
    skill_id: int
    level: int = 1
    years_of_experience: int = 0
    last_used: Optional[date] = None
    is_primary: bool = False


class ResumeSkillCreate(ResumeSkillBase):
    pass


class ResumeSkillUpdate(BaseModel):
    level: Optional[int] = None
    years_of_experience: Optional[int] = None
    last_used: Optional[date] = None
    is_primary: Optional[bool] = None


class ResumeSkillResponse(ResumeSkillBase):
    resume_id: int

    model_config = ConfigDict(from_attributes=True)