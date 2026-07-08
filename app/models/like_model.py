from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
)

from app.database.connection import Base


class Like(Base):

    __tablename__ = "likes"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    post_id = Column(
        Integer,
        ForeignKey("posts.id"),
        nullable=False
    )