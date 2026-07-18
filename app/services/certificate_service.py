from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.certificate import Certificate
from app.schemas.certificate import (
    CertificateCreate,
    CertificateUpdate,
)
from app.services.base_service import BaseService


class CertificateService(BaseService[Certificate]):
    def __init__(self) -> None:
        super().__init__(Certificate)

    def get_by_resume(
        self,
        db: Session,
        resume_id: int,
    ) -> list[Certificate]:
        statement = select(Certificate).where(
            Certificate.resume_id == resume_id,
        )

        return list(
            db.scalars(statement).all(),
        )

    def create_certificate(
        self,
        db: Session,
        certificate_data: CertificateCreate,
    ) -> Certificate:
        certificate = Certificate(
            **certificate_data.model_dump(),
        )

        return self.create(
            db=db,
            obj=certificate,
        )

    def update_certificate(
        self,
        db: Session,
        certificate: Certificate,
        certificate_data: CertificateUpdate,
    ) -> Certificate:
        update_data = certificate_data.model_dump(
            exclude_unset=True,
        )

        for field, value in update_data.items():
            setattr(
                certificate,
                field,
                value,
            )

        return self.update(
            db=db,
            obj=certificate,
        )


certificate_service = CertificateService()