from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.award import Award
from app.schemas.award import (
    AwardCreate,
    AwardUpdate,
)
from app.services.base_service import BaseService


class AwardService(BaseService[Award]):
    def __init__(self) -> None:
        super().__init__(Award)

    def get_by_resume(
        self,
        db: Session,
        resume_id: int,
    ) -> list[Award]:
        statement = select(Award).where(
            Award.resume_id == resume_id,
        )

        return list(
            db.scalars(statement).all(),
        )

    def create_award(
        self,
        db: Session,
        award_data: AwardCreate,
    ) -> Award:
        award = Award(
            **award_data.model_dump(),
        )

        return self.create(
            db=db,
            obj=award,
        )

    def update_award(
        self,
        db: Session,
        award: Award,
        award_data: AwardUpdate,
    ) -> Award:
        update_data = award_data.model_dump(
            exclude_unset=True,
        )

        for field, value in update_data.items():
            setattr(
                award,
                field,
                value,
            )

        return self.update(
            db=db,
            obj=award,
        )


award_service = AwardService()