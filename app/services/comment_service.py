from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.comment_model import Comment
from app.models.user_model import User

from app.repositories.comment_repository import (
    create_comment,
    get_comments_by_post,
    get_comment_by_id,
    update_comment,
    delete_comment,
)


def create_new_comment(
    db: Session,
    current_user: User,
    post_id: int,
    comment_data
):

    comment = Comment(
        user_id=current_user.id,
        post_id=post_id,
        content=comment_data.content
    )

    return create_comment(
        db,
        comment
    )


def view_comments(
    db: Session,
    post_id: int
):

    return get_comments_by_post(
        db,
        post_id
    )


def edit_comment(
    db: Session,
    current_user: User,
    comment_id: int,
    comment_data
):

    comment = get_comment_by_id(
        db,
        comment_id
    )

    if comment is None:
        raise HTTPException(
            status_code=404,
            detail="Comment not found"
        )

    if comment.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You can only update your own comments"
        )

    comment.content = comment_data.content

    return update_comment(
        db,
        comment
    )


def remove_comment(
    db: Session,
    current_user: User,
    comment_id: int
):

    comment = get_comment_by_id(
        db,
        comment_id
    )

    if comment is None:
        raise HTTPException(
            status_code=404,
            detail="Comment not found"
        )

    if comment.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You can only delete your own comments"
        )

    delete_comment(
        db,
        comment
    )

    return {
        "message": "Comment deleted successfully"
    }