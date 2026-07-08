from fastapi import FastAPI

from app.database.connection import (
    Base,
    engine,
)

from app.models.user_model import User
from app.models.profile_model import Profile

from app.routers.auth_router import (
    router as auth_router
)

from app.routers.profile_router import (
    router as profile_router
)

app = FastAPI(
    title="LinkedIn Lite API",
    version="1.0.0"
)

Base.metadata.create_all(
    bind=engine
)

app.include_router(
    auth_router
)

app.include_router(
    profile_router
)


@app.get("/")
def home():

    return {
        "message": "LinkedIn Lite API Running"
    }