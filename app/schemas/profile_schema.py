from pydantic import BaseModel


class ProfileCreate(BaseModel):
    headline: str
    company: str
    experience: str
    skills: str
    education: str
    location: str
    about: str
    profile_image: str


class ProfileUpdate(BaseModel):
    headline: str
    company: str
    experience: str
    skills: str
    education: str
    location: str
    about: str
    profile_image: str


class ProfileResponse(BaseModel):
    id: int
    user_id: int
    headline: str
    company: str
    experience: str
    skills: str
    education: str
    location: str
    about: str
    profile_image: str

    class Config:
        from_attributes = True