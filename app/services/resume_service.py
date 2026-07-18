from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.resume import Resume
from app.schemas.resume import (
    ResumeCreate,
    ResumeUpdate,
)
from app.services.base_service import BaseService


class ResumeService(BaseService[Resume]):
    def __init__(self) -> None:
        super().__init__(Resume)

    def get_by_user(
        self,
        db: Session,
        user_id: int,
    ) -> list[Resume]:
        statement = select(Resume).where(
            Resume.user_id == user_id,
        )

        return list(
            db.scalars(statement).all(),
        )

    def get_public_resumes(
        self,
        db: Session,
    ) -> list[Resume]:
        statement = select(Resume).where(
            Resume.is_public.is_(True),
        )

        return list(
            db.scalars(statement).all(),
        )

    def create_resume(
        self,
        db: Session,
        resume_data: ResumeCreate,
    ) -> Resume:
        resume = Resume(
            **resume_data.model_dump(),
        )

        return self.create(
            db=db,
            obj=resume,
        )

    def update_resume(
        self,
        db: Session,
        resume: Resume,
        resume_data: ResumeUpdate,
    ) -> Resume:
        update_data = resume_data.model_dump(
            exclude_unset=True,
        )

        for field, value in update_data.items():
            setattr(
                resume,
                field,
                value,
            )

        return self.update(
            db=db,
            obj=resume,
        )

    def mark_as_parsed(
        self,
        db: Session,
        resume: Resume,
    ) -> Resume:
        resume.parsed = True

        return self.update(
            db=db,
            obj=resume,
        )


resume_service = ResumeService()