from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import (
    get_current_active_user,
    get_current_admin,
)
from app.database.session import get_db
from app.schemas.experience import (
    ExperienceCreate,
    ExperienceResponse,
    ExperienceUpdate,
)
from app.services.experience_service import experience_service


router = APIRouter(
    prefix="/experiences",
    tags=["Experiences"],
)


@router.get(
    "/{experience_id}",
    response_model=ExperienceResponse,
)
def get_experience(
    experience_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    experience = experience_service.get(
        db=db,
        obj_id=experience_id,
    )

    if experience is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Experience not found",
        )

    return experience


@router.post(
    "/",
    response_model=ExperienceResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_experience(
    experience_data: ExperienceCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    return experience_service.create_experience(
        db=db,
        experience_data=experience_data,
    )


@router.put(
    "/{experience_id}",
    response_model=ExperienceResponse,
)
def update_experience(
    experience_id: int,
    experience_data: ExperienceUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    experience = experience_service.get(
        db=db,
        obj_id=experience_id,
    )

    if experience is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Experience not found",
        )

    return experience_service.update_experience(
        db=db,
        experience=experience,
        experience_data=experience_data,
    )


@router.delete(
    "/{experience_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_experience(
    experience_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin),
):
    experience = experience_service.get(
        db=db,
        obj_id=experience_id,
    )

    if experience is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Experience not found",
        )

    experience_service.delete(
        db=db,
        obj=experience,
    )