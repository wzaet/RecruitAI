from fastapi import APIRouter

from app.schemas.job import JobCreate
from app.services.job_service import create_job

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)


@router.get("/")
def list_jobs():
    return []


@router.post("/")
def add_job(job: JobCreate):
    return create_job(job)