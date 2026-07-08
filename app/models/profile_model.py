from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)

from sqlalchemy.orm import relationship

from app.database.connection import Base


class Profile(Base):

    __tablename__ = "profiles"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=True
    )

    headline = Column(String)
    company = Column(String)
    experience = Column(String)
    skills = Column(String)
    education = Column(String)
    location = Column(String)
    about = Column(String)
    profile_image = Column(String)

    user = relationship(
        "User",
        back_populates="profile"
    )