from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.award import (
    AwardCreate,
    AwardResponse,
    AwardUpdate,
)
from app.services.award_service import award_service

router = APIRouter(
    prefix="/awards",
    tags=["Awards"],
)


@router.get("/{award_id}", response_model=AwardResponse)
def get_award(
    award_id: int,
    db: Session = Depends(get_db),
):
    award = award_service.get(db=db, obj_id=award_id)

    if award is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Award not found",
        )

    return award


@router.post(
    "/",
    response_model=AwardResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_award(
    award_data: AwardCreate,
    db: Session = Depends(get_db),
):
    return award_service.create_award(
        db=db,
        award_data=award_data,
    )


@router.put("/{award_id}", response_model=AwardResponse)
def update_award(
    award_id: int,
    award_data: AwardUpdate,
    db: Session = Depends(get_db),
):
    award = award_service.get(db=db, obj_id=award_id)

    if award is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Award not found",
        )

    return award_service.update_award(
        db=db,
        award=award,
        award_data=award_data,
    )


@router.delete(
    "/{award_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_award(
    award_id: int,
    db: Session = Depends(get_db),
):
    award = award_service.get(db=db, obj_id=award_id)

    if award is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Award not found",
        )

    award_service.delete(db=db, obj=award)