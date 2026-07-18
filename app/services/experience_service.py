from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.experience import Experience
from app.schemas.experience import (
    ExperienceCreate,
    ExperienceUpdate,
)
from app.services.base_service import BaseService


class ExperienceService(BaseService[Experience]):
    def __init__(self) -> None:
        super().__init__(Experience)

    def get_by_resume(
        self,
        db: Session,
        resume_id: int,
    ) -> list[Experience]:
        statement = select(Experience).where(
            Experience.resume_id == resume_id,
        )

        return list(
            db.scalars(statement).all(),
        )

    def create_experience(
        self,
        db: Session,
        experience_data: ExperienceCreate,
    ) -> Experience:
        experience = Experience(
            **experience_data.model_dump(),
        )

        return self.create(
            db=db,
            obj=experience,
        )

    def update_experience(
        self,
        db: Session,
        experience: Experience,
        experience_data: ExperienceUpdate,
    ) -> Experience:
        update_data = experience_data.model_dump(
            exclude_unset=True,
        )

        for field, value in update_data.items():
            setattr(
                experience,
                field,
                value,
            )

        return self.update(
            db=db,
            obj=experience,
        )


experience_service = ExperienceService()