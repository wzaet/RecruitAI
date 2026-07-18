from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import (
    get_current_active_user,
    get_current_admin,
)
from app.database.session import get_db
from app.schemas.education import (
    EducationCreate,
    EducationResponse,
    EducationUpdate,
)
from app.services.education_service import education_service


router = APIRouter(
    prefix="/educations",
    tags=["Educations"],
)


@router.get(
    "/{education_id}",
    response_model=EducationResponse,
)
def get_education(
    education_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    education = education_service.get(
        db=db,
        obj_id=education_id,
    )

    if education is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Education not found",
        )

    return education


@router.post(
    "/",
    response_model=EducationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_education(
    education_data: EducationCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    return education_service.create_education(
        db=db,
        education_data=education_data,
    )


@router.put(
    "/{education_id}",
    response_model=EducationResponse,
)
def update_education(
    education_id: int,
    education_data: EducationUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    education = education_service.get(
        db=db,
        obj_id=education_id,
    )

    if education is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Education not found",
        )

    return education_service.update_education(
        db=db,
        education=education,
        education_data=education_data,
    )


@router.delete(
    "/{education_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_education(
    education_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin),
):
    education = education_service.get(
        db=db,
        obj_id=education_id,
    )

    if education is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Education not found",
        )

    education_service.delete(
        db=db,
        obj=education,
    )