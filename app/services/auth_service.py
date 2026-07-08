from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user_model import User
from app.repositories.user_repository import (
    get_user_by_email,
    create_user,
)

from app.utils.hash import (
    hash_password,
    verify_password,
)

from app.utils.token import (
    create_access_token,
    create_refresh_token,
    verify_token,
)


def register_user(
    db: Session,
    user
):

    existing_user = get_user_by_email(
        db,
        user.email
    )

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(
            user.password
        ),
        role="user"
    )

    return create_user(
        db,
        new_user
    )


def login_user(
    db: Session,
    user
):

    existing_user = get_user_by_email(
        db,
        user.email
    )

    if not existing_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        user.password,
        existing_user.password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        {
            "sub": existing_user.email,
            "role": existing_user.role
        }
    )

    refresh_token = create_refresh_token(
        {
            "sub": existing_user.email,
            "role": existing_user.role
        }
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


def refresh_access_token(
    refresh_token: str
):

    payload = verify_token(
        refresh_token
    )

    if payload is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid Refresh Token"
        )

    email = payload.get("sub")

    access_token = create_access_token(
        {
            "sub": email,
            "role": payload.get(
                "role",
                "user"
            )
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }