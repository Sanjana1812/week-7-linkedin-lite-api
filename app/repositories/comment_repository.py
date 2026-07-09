from sqlalchemy.orm import Session

from app.models.comment_model import Comment


def create_comment(
    db: Session,
    comment: Comment
):
    db.add(comment)
    db.commit()
    db.refresh(comment)

    return comment


def get_comments_by_post(
    db: Session,
    post_id: int
):
    return (
        db.query(Comment)
        .filter(
            Comment.post_id == post_id
        )
        .all()
    )


def get_comment_by_id(
    db: Session,
    comment_id: int
):
    return (
        db.query(Comment)
        .filter(
            Comment.id == comment_id
        )
        .first()
    )


def update_comment(
    db: Session,
    comment: Comment
):
    db.commit()
    db.refresh(comment)

    return comment


def delete_comment(
    db: Session,
    comment: Comment
):
    db.delete(comment)
    db.commit()