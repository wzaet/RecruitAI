from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.education import Education
from app.schemas.education import (
    EducationCreate,
    EducationUpdate,
)
from app.services.base_service import BaseService


class EducationService(BaseService[Education]):
    def __init__(self) -> None:
        super().__init__(Education)

    def get_by_resume(
        self,
        db: Session,
        resume_id: int,
    ) -> list[Education]:
        statement = select(Education).where(
            Education.resume_id == resume_id,
        )

        return list(db.scalars(statement))

    def create_education(
        self,
        db: Session,
        education_data: EducationCreate,
    ) -> Education:
        education = Education(
            **education_data.model_dump(),
        )

        return self.create(
            db=db,
            obj=education,
        )

    def update_education(
        self,
        db: Session,
        education: Education,
        education_data: EducationUpdate,
    ) -> Education:
        update_data = education_data.model_dump(
            exclude_unset=True,
        )

        for field, value in update_data.items():
            setattr(
                education,
                field,
                value,
            )

        return self.update(
            db=db,
            obj=education,
        )


education_service = EducationService()