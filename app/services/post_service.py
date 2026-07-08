from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.post_model import Post
from app.models.user_model import User

from app.repositories.post_repository import (
    create_post,
    get_all_posts,
    get_post_by_id,
    update_post,
    delete_post,
)


def create_new_post(
    db: Session,
    current_user: User,
    post_data
):

    post = Post(
        user_id=current_user.id,
        content=post_data.content
    )

    return create_post(
        db,
        post
    )


def view_all_posts(
    db: Session
):

    return get_all_posts(
        db
    )


def view_post(
    db: Session,
    post_id: int
):

    post = get_post_by_id(
        db,
        post_id
    )

    if post is None:

        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )

    return post


def edit_post(
    db: Session,
    current_user: User,
    post_id: int,
    post_data
):

    post = get_post_by_id(
        db,
        post_id
    )

    if post is None:

        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )

    if post.user_id != current_user.id:

        raise HTTPException(
            status_code=403,
            detail="You can only update your own posts"
        )

    post.content = post_data.content

    return update_post(
        db,
        post
    )


def remove_post(
    db: Session,
    current_user: User,
    post_id: int
):

    post = get_post_by_id(
        db,
        post_id
    )

    if post is None:

        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )

    if post.user_id != current_user.id:

        raise HTTPException(
            status_code=403,
            detail="You can only delete your own posts"
        )

    delete_post(
        db,
        post
    )

    return {
        "message": "Post deleted successfully"
    }