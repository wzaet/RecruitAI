from fastapi import FastAPI

from app.routers.jobs import router as jobs_router

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