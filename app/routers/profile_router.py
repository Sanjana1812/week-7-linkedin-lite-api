from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.user_model import User

from app.schemas.profile_schema import (
    ProfileCreate,
    ProfileResponse,
)

from app.services.profile_service import (
    get_profile,
    save_profile,
)

from app.utils.auth import get_current_user

router = APIRouter(
    prefix="",
    tags=["Profile"]
)


@router.get(
    "/profile",
    response_model=ProfileResponse
)
def view_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_profile(
        db,
        current_user
    )


@router.put(
    "/profile",
    response_model=ProfileResponse
)
def update_profile(
    profile: ProfileCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return save_profile(
        db,
        current_user,
        profile
    )