from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.database.session import SessionLocal
from app.models.user import User

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def register_user(
    full_name: str,
    email: str,
    phone: str,
    password: str,
    role: str = "candidate"
):
    db: Session = SessionLocal()

    try:
        existing = db.query(User).filter(
            User.email == email
        ).first()

        if existing:
            return {
                "error": "Email already exists"
            }

        user = User(
            full_name=full_name,
            email=email,
            phone=phone,
            password=hash_password(password),
            role=role
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return {
            "id": user.id,
            "message": "User registered successfully"
        }

    finally:
        db.close()


def authenticate_user(
    email: str,
    password: str
):
    db: Session = SessionLocal()

    try:
        user = db.query(User).filter(
            User.email == email
        ).first()

        if not user:
            return None

        if not verify_password(
            password,
            user.password
        ):
            return None

        return user

    finally:
        db.close()