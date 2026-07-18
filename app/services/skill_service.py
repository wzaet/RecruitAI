from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.skill import Skill
from app.schemas.skill import (
    SkillCreate,
    SkillUpdate,
)
from app.services.base_service import BaseService


class SkillService(BaseService[Skill]):
    def __init__(self) -> None:
        super().__init__(Skill)

    def get_by_name(
        self,
        db: Session,
        name: str,
    ) -> Skill | None:
        statement = select(Skill).where(
            Skill.name == name,
        )

        return db.scalar(statement)

    def create_skill(
        self,
        db: Session,
        skill_data: SkillCreate,
    ) -> Skill:
        skill = Skill(
            **skill_data.model_dump(),
        )

        return self.create(
            db=db,
            obj=skill,
        )

    def update_skill(
        self,
        db: Session,
        skill: Skill,
        skill_data: SkillUpdate,
    ) -> Skill:
        update_data = skill_data.model_dump(
            exclude_unset=True,
        )

        for field, value in update_data.items():
            setattr(
                skill,
                field,
                value,
            )

        return self.update(
            db=db,
            obj=skill,
        )


skill_service = SkillService()