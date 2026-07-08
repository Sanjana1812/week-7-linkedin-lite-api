from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.user_model import User

from app.schemas.like_schema import (
    LikeResponse,
    LikeCountResponse,
)

from app.services.like_service import (
    like_post,
    unlike_post,
    get_post_likes,
)

from app.utils.auth import get_current_user

router = APIRouter(
    prefix="",
    tags=["Likes"]
)


@router.post(
    "/posts/{post_id}/like",
    response_model=LikeResponse
)
def like(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return like_post(
        db,
        current_user.id,
        post_id
    )


@router.delete(
    "/posts/{post_id}/like",
    response_model=LikeResponse
)
def unlike(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return unlike_post(
        db,
        current_user.id,
        post_id
    )


@router.get(
    "/posts/{post_id}/likes",
    response_model=LikeCountResponse
)
def total_likes(
    post_id: int,
    db: Session = Depends(get_db)
):
    return get_post_likes(
        db,
        post_id
    )