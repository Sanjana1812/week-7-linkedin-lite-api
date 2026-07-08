from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.like_model import Like

from app.repositories.like_repository import (
    get_like,
    create_like,
    delete_like,
    count_likes,
)


def like_post(
    db: Session,
    user_id: int,
    post_id: int
):

    existing_like = get_like(
        db,
        user_id,
        post_id
    )

    if existing_like:
        raise HTTPException(
            status_code=400,
            detail="Post already liked"
        )

    like = Like(
        user_id=user_id,
        post_id=post_id
    )

    create_like(
        db,
        like
    )

    return {
        "message": "Post liked successfully"
    }


def unlike_post(
    db: Session,
    user_id: int,
    post_id: int
):

    existing_like = get_like(
        db,
        user_id,
        post_id
    )

    if not existing_like:
        raise HTTPException(
            status_code=404,
            detail="Like not found"
        )

    delete_like(
        db,
        existing_like
    )

    return {
        "message": "Post unliked successfully"
    }


def get_post_likes(
    db: Session,
    post_id: int
):

    total = count_likes(
        db,
        post_id
    )

    return {
        "post_id": post_id,
        "likes": total
    }