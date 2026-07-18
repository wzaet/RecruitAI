from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.company_member import (
    CompanyMemberCreate,
    CompanyMemberResponse,
    CompanyMemberUpdate,
)
from app.services.company_member_service import company_member_service

router = APIRouter(
    prefix="/company-members",
    tags=["Company Members"],
)


@router.get(
    "/{member_id}",
    response_model=CompanyMemberResponse,
)
def get_company_member(
    member_id: int,
    db: Session = Depends(get_db),
):
    member = company_member_service.get(
        db=db,
        obj_id=member_id,
    )

    if member is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company member not found",
        )

    return member


@router.post(
    "/",
    response_model=CompanyMemberResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_company_member(
    member_data: CompanyMemberCreate,
    db: Session = Depends(get_db),
):
    return company_member_service.create_membership(
        db=db,
        member_data=member_data,
    )


@router.put(
    "/{member_id}",
    response_model=CompanyMemberResponse,
)
def update_company_member(
    member_id: int,
    member_data: CompanyMemberUpdate,
    db: Session = Depends(get_db),
):
    member = company_member_service.get(
        db=db,
        obj_id=member_id,
    )

    if member is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company member not found",
        )

    return company_member_service.update_membership(
        db=db,
        member=member,
        member_data=member_data,
    )


@router.delete(
    "/{member_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_company_member(
    member_id: int,
    db: Session = Depends(get_db),
):
    member = company_member_service.get(
        db=db,
        obj_id=member_id,
    )

    if member is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Company member not found",
        )

    company_member_service.delete(
        db=db,
        obj=member,
    )