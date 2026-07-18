from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.resume_link import (
    ResumeLinkCreate,
    ResumeLinkResponse,
    ResumeLinkUpdate,
)
from app.services.resume_link_service import resume_link_service

router = APIRouter(
    prefix="/resume-links",
    tags=["Resume Links"],
)


@router.get("/{link_id}", response_model=ResumeLinkResponse)
def get_resume_link(
    link_id: int,
    db: Session = Depends(get_db),
):
    link = resume_link_service.get(db=db, obj_id=link_id)

    if link is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume link not found",
        )

    return link


@router.post(
    "/",
    response_model=ResumeLinkResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_resume_link(
    link_data: ResumeLinkCreate,
    db: Session = Depends(get_db),
):
    return resume_link_service.create_resume_link(
        db=db,
        link_data=link_data,
    )


@router.put("/{link_id}", response_model=ResumeLinkResponse)
def update_resume_link(
    link_id: int,
    link_data: ResumeLinkUpdate,
    db: Session = Depends(get_db),
):
    link = resume_link_service.get(db=db, obj_id=link_id)

    if link is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume link not found",
        )

    return resume_link_service.update_resume_link(
        db=db,
        link=link,
        link_data=link_data,
    )


@router.delete(
    "/{link_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_resume_link(
    link_id: int,
    db: Session = Depends(get_db),
):
    link = resume_link_service.get(db=db, obj_id=link_id)

    if link is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume link not found",
        )

    resume_link_service.delete(db=db, obj=link)