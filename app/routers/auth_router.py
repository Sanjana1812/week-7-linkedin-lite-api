from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.user_model import User

from app.schemas.user_schema import (
    UserRegister,
    UserResponse,
    UserLogin,
    TokenResponse,
    RefreshTokenRequest,
    AccessTokenResponse,
    UserProfile,
)

from app.services.auth_service import (
    register_user,
    login_user,
    refresh_access_token,
)

from app.utils.auth import get_current_user

router = APIRouter(
    prefix="",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=201
)
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    return register_user(db, user)


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    return login_user(db, user)


@router.post(
    "/refresh-token",
    response_model=AccessTokenResponse
)
def refresh_token(
    token: RefreshTokenRequest
):
    return refresh_access_token(
        token.refresh_token
    )


@router.get(
    "/me",
    response_model=UserProfile
)
def get_me(
    current_user: User = Depends(get_current_user)
):
    return current_user