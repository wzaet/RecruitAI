from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.services.base_service import BaseService


class UserService(BaseService[User]):
    def __init__(self) -> None:
        super().__init__(User)

    def get_by_email(
        self,
        db: Session,
        email: str,
    ) -> User | None:
        statement = select(User).where(User.email == email)
        return db.scalar(statement)

    def get_by_username(
        self,
        db: Session,
        username: str,
    ) -> User | None:
        statement = select(User).where(User.username == username)
        return db.scalar(statement)

    def email_exists(
        self,
        db: Session,
        email: str,
    ) -> bool:
        return self.get_by_email(db, email) is not None

    def username_exists(
        self,
        db: Session,
        username: str,
    ) -> bool:
        return self.get_by_username(db, username) is not None

    def create_user(
        self,
        db: Session,
        user_data: UserCreate,
    ) -> User:
        user = User(
            **user_data.model_dump(),
        )

        return self.create(
            db=db,
            obj=user,
        )

    def update_user(
        self,
        db: Session,
        user: User,
        user_data: UserUpdate,
    ) -> User:
        update_data = user_data.model_dump(
            exclude_unset=True,
        )

        for field, value in update_data.items():
            setattr(
                user,
                field,
                value,
            )

        return self.update(
            db=db,
            obj=user,
        )


user_service = UserService()