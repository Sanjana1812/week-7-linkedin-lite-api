from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.user_model import User

from app.schemas.comment_schema import (
    CommentCreate,
    CommentUpdate,
    CommentResponse,
)

from app.services.comment_service import (
    create_new_comment,
    view_comments,
    edit_comment,
    remove_comment,
)

from app.utils.auth import get_current_user

router = APIRouter(
    prefix="",
    tags=["Comments"]
)


@router.post(
    "/posts/{post_id}/comments",
    response_model=CommentResponse,
    status_code=201
)
def create_comment(
    post_id: int,
    comment: CommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_new_comment(
        db,
        current_user,
        post_id,
        comment
    )


@router.get(
    "/posts/{post_id}/comments",
    response_model=list[CommentResponse]
)
def get_comments(
    post_id: int,
    db: Session = Depends(get_db)
):
    return view_comments(
        db,
        post_id
    )


@router.put(
    "/comments/{comment_id}",
    response_model=CommentResponse
)
def update_comment(
    comment_id: int,
    comment: CommentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return edit_comment(
        db,
        current_user,
        comment_id,
        comment
    )


@router.delete(
    "/comments/{comment_id}"
)
def delete_comment(
    comment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return remove_comment(
        db,
        current_user,
        comment_id
    )