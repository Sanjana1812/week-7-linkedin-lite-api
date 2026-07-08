from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.like_model import Like


def get_like(
    db: Session,
    user_id: int,
    post_id: int
):
    return (
        db.query(Like)
        .filter(
            Like.user_id == user_id,
            Like.post_id == post_id
        )
        .first()
    )


def create_like(
    db: Session,
    like: Like
):
    db.add(like)
    db.commit()
    db.refresh(like)
    return like


def delete_like(
    db: Session,
    like: Like
):
    db.delete(like)
    db.commit()


def count_likes(
    db: Session,
    post_id: int
):
    return (
        db.query(func.count(Like.id))
        .filter(
            Like.post_id == post_id
        )
        .scalar()
    )