from fastapi import FastAPI

from app.database.base import Base
from app.database.session import engine

from app.models.job import Job
from app.routers.jobs import router as jobs_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="RecruitAI",
    version="0.1.0",
    description="AI-powered recruitment platform"
)

app.include_router(jobs_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to RecruitAI"
    }