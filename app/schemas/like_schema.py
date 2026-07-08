from pydantic import BaseModel


class LikeResponse(BaseModel):

    message: str


class LikeCountResponse(BaseModel):

    post_id: int
    likes: int

    class Config:
        from_attributes = True