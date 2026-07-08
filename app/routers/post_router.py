from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.user_model import User

from app.schemas.post_schema import (
    PostCreate,
    PostUpdate,
    PostResponse,
)

from app.services.post_service import (
    create_new_post,
    view_all_posts,
    view_post,
    edit_post,
    remove_post,
)

from app.utils.auth import get_current_user

router = APIRouter(
    prefix="",
    tags=["Posts"]
)


@router.post(
    "/posts",
    response_model=PostResponse,
    status_code=201
)
def create_post(
    post: PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_new_post(
        db,
        current_user,
        post
    )


@router.get(
    "/posts",
    response_model=list[PostResponse]
)
def get_posts(
    db: Session = Depends(get_db)
):
    return view_all_posts(db)


@router.get(
    "/posts/{post_id}",
    response_model=PostResponse
)
def get_post(
    post_id: int,
    db: Session = Depends(get_db)
):
    return view_post(
        db,
        post_id
    )


@router.put(
    "/posts/{post_id}",
    response_model=PostResponse
)
def update_post(
    post_id: int,
    post: PostUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return edit_post(
        db,
        current_user,
        post_id,
        post
    )


@router.delete(
    "/posts/{post_id}"
)
def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return remove_post(
        db,
        current_user,
        post_id
    )