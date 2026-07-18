from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.language import (
    LanguageCreate,
    LanguageResponse,
    LanguageUpdate,
)
from app.services.language_service import language_service

router = APIRouter(
    prefix="/languages",
    tags=["Languages"],
)


@router.get("/{language_id}", response_model=LanguageResponse)
def get_language(
    language_id: int,
    db: Session = Depends(get_db),
):
    language = language_service.get(db=db, obj_id=language_id)

    if language is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Language not found",
        )

    return language


@router.post(
    "/",
    response_model=LanguageResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_language(
    language_data: LanguageCreate,
    db: Session = Depends(get_db),
):
    return language_service.create_language(
        db=db,
        language_data=language_data,
    )


@router.put("/{language_id}", response_model=LanguageResponse)
def update_language(
    language_id: int,
    language_data: LanguageUpdate,
    db: Session = Depends(get_db),
):
    language = language_service.get(db=db, obj_id=language_id)

    if language is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Language not found",
        )

    return language_service.update_language(
        db=db,
        language=language,
        language_data=language_data,
    )


@router.delete(
    "/{language_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_language(
    language_id: int,
    db: Session = Depends(get_db),
):
    language = language_service.get(db=db, obj_id=language_id)

    if language is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Language not found",
        )

    language_service.delete(db=db, obj=language)