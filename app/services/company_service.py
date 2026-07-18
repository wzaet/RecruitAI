from sqlalchemy.orm import Session

from app.models.company import Company
from app.schemas.company import (
    CompanyCreate,
    CompanyUpdate,
)


class CompanyService:

    def get(
        self,
        db: Session,
        obj_id: int,
    ):
        return (
            db.query(Company)
            .filter(Company.id == obj_id)
            .first()
        )

    def get_all(
        self,
        db: Session,
    ):
        return db.query(Company).all()

    def create_company(
        self,
        db: Session,
        company_data: CompanyCreate,
    ):
        company = Company(
            **company_data.model_dump()
        )

        db.add(company)
        db.commit()
        db.refresh(company)

        return company

    def update_company(
        self,
        db: Session,
        company: Company,
        company_data: CompanyUpdate,
    ):
        update_data = company_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                company,
                key,
                value,
            )

        db.commit()
        db.refresh(company)

        return company

    def delete(
        self,
        db: Session,
        obj: Company,
    ):
        db.delete(obj)
        db.commit()


company_service = CompanyService()