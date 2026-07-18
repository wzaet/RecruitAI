from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.reference import Reference
from app.schemas.reference import ReferenceCreate, ReferenceUpdate
from app.services.base_service import BaseService


class ReferenceService(BaseService[Reference]):
    def __init__(self) -> None:
        super().__init__(Reference)

    def get_by_resume(
        self,
        db: Session,
        resume_id: int,
    ) -> list[Reference]:
        statement = select(Reference).where(Reference.resume_id == resume_id)
        return list(db.scalars(statement))

    def create_reference(
        self,
        db: Session,
        reference_data: ReferenceCreate,
    ) -> Reference:
        reference = Reference(**reference_data.model_dump())
        return self.create(db=db, obj=reference)

    def update_reference(
        self,
        db: Session,
        reference: Reference,
        reference_data: ReferenceUpdate,
    ) -> Reference:
        update_data = reference_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(reference, field, value)

        return self.update(db=db, obj=reference)


reference_service = ReferenceService()