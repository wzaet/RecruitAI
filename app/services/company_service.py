from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate
from app.services.base_service import BaseService


class CompanyService(BaseService[Company]):
    def __init__(self) -> None:
        super().__init__(Company)

    def get_by_slug(
        self,
        db: Session,
        slug: str,
    ) -> Company | None:
        statement = select(Company).where(
            Company.slug == slug,
        )
        return db.scalar(statement)

    def slug_exists(
        self,
        db: Session,
        slug: str,
    ) -> bool:
        return self.get_by_slug(
            db,
            slug,
        ) is not None

    def create_company(
        self,
        db: Session,
        company_data: CompanyCreate,
    ) -> Company:
        company = Company(
            **company_data.model_dump(),
        )

        return self.create(
            db=db,
            obj=company,
        )

    def update_company(
        self,
        db: Session,
        company: Company,
        company_data: CompanyUpdate,
    ) -> Company:
        update_data = company_data.model_dump(
            exclude_unset=True,
        )

        for field, value in update_data.items():
            setattr(
                company,
                field,
                value,
            )

        return self.update(
            db=db,
            obj=company,
        )


company_service = CompanyService()