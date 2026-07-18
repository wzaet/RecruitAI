from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.schemas.user import UserCreate
from app.services.user_service import user_service


class AuthService:
    def register(
        self,
        db: Session,
        user_data: UserCreate,
    ):
        """
        Register a new user.
        """

        if user_service.email_exists(db, user_data.email):
            raise ValueError("Email already registered.")

        hashed_password = hash_password(user_data.password)

        return user_service.create_user(
            db=db,
            user_data=user_data,
            hashed_password=hashed_password,
        )

    def login(
        self,
        db: Session,
        email: str,
        password: str,
    ) -> str:
        """
        Authenticate a user and return a JWT access token.
        """

        user = user_service.get_by_email(
            db,
            email,
        )

        if not user:
            raise ValueError("Invalid email or password.")

        if not verify_password(
            password,
            user.hashed_password,
        ):
            raise ValueError("Invalid email or password.")

        return create_access_token(
            subject=user.id,
        )


auth_service = AuthService()