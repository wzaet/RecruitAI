from fastapi import APIRouter, HTTPException

from app.schemas.user import UserRegister, UserLogin
from app.services.user_service import (
    register_user,
    authenticate_user,
)
from app.core.security import create_access_token

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/register")
def register(user: UserRegister):
    result = register_user(
        full_name=user.full_name,
        email=user.email,
        phone=user.phone,
        password=user.password,
        role=user.role,
    )

    if "error" in result:
        raise HTTPException(
            status_code=400,
            detail=result["error"]
        )

    return result


@router.post("/login")
def login(user: UserLogin):
    db_user = authenticate_user(
        user.email,
        user.password
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token(
        {
            "sub": str(db_user.id),
            "role": db_user.role,
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": db_user.id,
            "full_name": db_user.full_name,
            "email": db_user.email,
            "role": db_user.role,
        },
    }