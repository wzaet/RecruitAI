from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.reference import (
    ReferenceCreate,
    ReferenceResponse,
    ReferenceUpdate,
)
from app.services.reference_service import reference_service

router = APIRouter(
    prefix="/references",
    tags=["References"],
)


@router.get("/{reference_id}", response_model=ReferenceResponse)
def get_reference(
    reference_id: int,
    db: Session = Depends(get_db),
):
    reference = reference_service.get(db=db, obj_id=reference_id)

    if reference is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reference not found",
        )

    return reference


@router.post(
    "/",
    response_model=ReferenceResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_reference(
    reference_data: ReferenceCreate,
    db: Session = Depends(get_db),
):
    return reference_service.create_reference(
        db=db,
        reference_data=reference_data,
    )


@router.put("/{reference_id}", response_model=ReferenceResponse)
def update_reference(
    reference_id: int,
    reference_data: ReferenceUpdate,
    db: Session = Depends(get_db),
):
    reference = reference_service.get(db=db, obj_id=reference_id)

    if reference is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reference not found",
        )

    return reference_service.update_reference(
        db=db,
        reference=reference,
        reference_data=reference_data,
    )


@router.delete(
    "/{reference_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_reference(
    reference_id: int,
    db: Session = Depends(get_db),
):
    reference = reference_service.get(db=db, obj_id=reference_id)

    if reference is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reference not found",
        )

    reference_service.delete(db=db, obj=reference)