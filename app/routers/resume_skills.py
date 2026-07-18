from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import (
    get_current_active_user,
    get_current_admin,
)
from app.database.session import get_db
from app.schemas.resume_skill import (
    ResumeSkillCreate,
    ResumeSkillResponse,
    ResumeSkillUpdate,
)
from app.services.resume_skill_service import resume_skill_service


router = APIRouter(
    prefix="/resume-skills",
    tags=["Resume Skills"],
)


@router.get(
    "/{resume_skill_id}",
    response_model=ResumeSkillResponse,
)
def get_resume_skill(
    resume_skill_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    resume_skill = resume_skill_service.get(
        db=db,
        obj_id=resume_skill_id,
    )

    if resume_skill is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume skill not found",
        )

    return resume_skill


@router.post(
    "/",
    response_model=ResumeSkillResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_resume_skill(
    resume_skill_data: ResumeSkillCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    return resume_skill_service.create_resume_skill(
        db=db,
        resume_skill_data=resume_skill_data,
    )


@router.put(
    "/{resume_skill_id}",
    response_model=ResumeSkillResponse,
)
def update_resume_skill(
    resume_skill_id: int,
    resume_skill_data: ResumeSkillUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    resume_skill = resume_skill_service.get(
        db=db,
        obj_id=resume_skill_id,
    )

    if resume_skill is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume skill not found",
        )

    return resume_skill_service.update_resume_skill(
        db=db,
        resume_skill=resume_skill,
        resume_skill_data=resume_skill_data,
    )


@router.delete(
    "/{resume_skill_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_resume_skill(
    resume_skill_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_admin),
):
    resume_skill = resume_skill_service.get(
        db=db,
        obj_id=resume_skill_id,
    )

    if resume_skill is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume skill not found",
        )

    resume_skill_service.delete(
        db=db,
        obj=resume_skill,
    )