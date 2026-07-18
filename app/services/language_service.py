from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.language import Language
from app.schemas.language import (
    LanguageCreate,
    LanguageUpdate,
)
from app.services.base_service import BaseService


class LanguageService(BaseService[Language]):
    def __init__(self) -> None:
        super().__init__(Language)

    def get_by_resume(
        self,
        db: Session,
        resume_id: int,
    ) -> list[Language]:
        statement = select(Language).where(
            Language.resume_id == resume_id,
        )

        return list(
            db.scalars(statement).all(),
        )

    def create_language(
        self,
        db: Session,
        language_data: LanguageCreate,
    ) -> Language:
        language = Language(
            **language_data.model_dump(),
        )

        return self.create(
            db=db,
            obj=language,
        )

    def update_language(
        self,
        db: Session,
        language: Language,
        language_data: LanguageUpdate,
    ) -> Language:
        update_data = language_data.model_dump(
            exclude_unset=True,
        )

        for field, value in update_data.items():
            setattr(
                language,
                field,
                value,
            )

        return self.update(
            db=db,
            obj=language,
        )


language_service = LanguageService()