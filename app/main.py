from fastapi import FastAPI

from app.database.base import Base
from app.database.session import engine
from app.models import Job, User
from app.routers.jobs import router as jobs_router
from app.routers.applicants import router as applicants_router
from app.routers.users import router as users_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="RecruitAI",
    version="0.1.0",
    description="AI-powered recruitment platform"
)

app.include_router(users_router)
app.include_router(jobs_router)
app.include_router(applicants_router)
@app.get("/")
def root():
    return {
        "message": "Welcome to RecruitAI"
    }