from pydantic import BaseModel
from datetime import datetime


class PostCreate(BaseModel):
    content: str


class PostUpdate(BaseModel):
    content: str


class PostResponse(BaseModel):
    id: int
    user_id: int
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True