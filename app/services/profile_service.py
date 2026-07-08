from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.profile_model import Profile
from app.models.user_model import User

from app.repositories.profile_repository import (
    get_profile_by_user_id,
    create_profile,
    update_profile,
)


def get_profile(
    db: Session,
    current_user: User
):

    profile = get_profile_by_user_id(
        db,
        current_user.id
    )

    if profile is None:
        raise HTTPException(
            status_code=404,
            detail="Profile not found"
        )

    return profile


def save_profile(
    db: Session,
    current_user: User,
    profile_data
):

    profile = get_profile_by_user_id(
        db,
        current_user.id
    )

    if profile is None:

        profile = Profile(
            user_id=current_user.id,
            headline=profile_data.headline,
            company=profile_data.company,
            experience=profile_data.experience,
            skills=profile_data.skills,
            education=profile_data.education,
            location=profile_data.location,
            about=profile_data.about,
            profile_image=profile_data.profile_image
        )

        return create_profile(
            db,
            profile
        )

    profile.headline = profile_data.headline
    profile.company = profile_data.company
    profile.experience = profile_data.experience
    profile.skills = profile_data.skills
    profile.education = profile_data.education
    profile.location = profile_data.location
    profile.about = profile_data.about
    profile.profile_image = profile_data.profile_image

    return update_profile(
        db,
        profile
    )