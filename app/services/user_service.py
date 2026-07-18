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
        statement = select(User).where(
            User.email == email,
        )
        return db.scalar(statement)

    def email_exists(
        self,
        db: Session,
        email: str,
    ) -> bool:
        return self.get_by_email(
            db=db,
            email=email,
        ) is not None

    def create_user(
        self,
        db: Session,
        user_data: UserCreate,
        hashed_password: str,
    ) -> User:
        user = User(
            full_name=user_data.full_name,
            email=user_data.email,
            phone=user_data.phone,
            hashed_password=hashed_password,
            role=user_data.role,
            is_active=user_data.is_active,
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

        update_data.pop(
            "password",
            None,
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