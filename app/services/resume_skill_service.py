from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.resume_skill import ResumeSkill
from app.schemas.resume_skill import ResumeSkillCreate, ResumeSkillUpdate
from app.services.base_service import BaseService


class ResumeSkillService(BaseService[ResumeSkill]):
    def __init__(self) -> None:
        super().__init__(ResumeSkill)

    def get_by_resume(
        self,
        db: Session,
        resume_id: int,
    ) -> list[ResumeSkill]:
        statement = select(ResumeSkill).where(
            ResumeSkill.resume_id == resume_id,
        )

        return list(db.scalars(statement))

    def create_resume_skill(
        self,
        db: Session,
        skill_data: ResumeSkillCreate,
    ) -> ResumeSkill:
        skill = ResumeSkill(**skill_data.model_dump())
        return self.create(db=db, obj=skill)

    def update_resume_skill(
        self,
        db: Session,
        skill: ResumeSkill,
        skill_data: ResumeSkillUpdate,
    ) -> ResumeSkill:
        update_data = skill_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(skill, field, value)

        return self.update(db=db, obj=skill)


resume_skill_service = ResumeSkillService()