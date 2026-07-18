from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.company_member import CompanyMember
from app.schemas.company_member import (
    CompanyMemberCreate,
    CompanyMemberUpdate,
)
from app.services.base_service import BaseService


class CompanyMemberService(BaseService[CompanyMember]):
    def __init__(self) -> None:
        super().__init__(CompanyMember)

    def get_members_by_company(
        self,
        db: Session,
        company_id: int,
    ) -> list[CompanyMember]:
        statement = select(CompanyMember).where(
            CompanyMember.company_id == company_id,
        )

        return list(db.scalars(statement))

    def get_membership(
        self,
        db: Session,
        company_id: int,
        user_id: int,
    ) -> CompanyMember | None:
        statement = select(CompanyMember).where(
            CompanyMember.company_id == company_id,
            CompanyMember.user_id == user_id,
        )

        return db.scalar(statement)

    def create_membership(
        self,
        db: Session,
        membership_data: CompanyMemberCreate,
    ) -> CompanyMember:
        membership = CompanyMember(
            **membership_data.model_dump(),
        )

        return self.create(
            db=db,
            obj=membership,
        )

    def update_membership(
        self,
        db: Session,
        membership: CompanyMember,
        membership_data: CompanyMemberUpdate,
    ) -> CompanyMember:
        update_data = membership_data.model_dump(
            exclude_unset=True,
        )

        for field, value in update_data.items():
            setattr(
                membership,
                field,
                value,
            )

        return self.update(
            db=db,
            obj=membership,
        )


company_member_service = CompanyMemberService()