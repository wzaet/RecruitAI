from typing import Generic, TypeVar

from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase, Session

ModelType = TypeVar("ModelType", bound=DeclarativeBase)


class BaseService(Generic[ModelType]):
    """
    Base service for shared database operations.
    """

    def __init__(self, model: type[ModelType]) -> None:
        self.model = model

    def get(
        self,
        db: Session,
        obj_id: int,
    ) -> ModelType | None:
        statement = select(self.model).where(self.model.id == obj_id)
        return db.scalar(statement)

    def get_all(
        self,
        db: Session,
    ) -> list[ModelType]:
        statement = select(self.model)
        return list(db.scalars(statement))

    def create(
        self,
        db: Session,
        obj: ModelType,
    ) -> ModelType:
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def update(
        self,
        db: Session,
        obj: ModelType,
    ) -> ModelType:
        db.commit()
        db.refresh(obj)
        return obj

    def delete(
        self,
        db: Session,
        obj: ModelType,
    ) -> None:
        db.delete(obj)
        db.commit()