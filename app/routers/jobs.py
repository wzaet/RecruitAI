from fastapi import APIRouter

from app.schemas.job import JobCreate, JobUpdate
from app.services.job_service import (
    create_job,
    get_jobs,
    update_job,
    delete_job,
)

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)

@router.get("/")
def list_jobs():
    return get_jobs()


@router.post("/")
def add_job(job: JobCreate):
    return create_job(job)


@router.put("/{job_id}")
def edit_job(job_id: int, job: JobUpdate):
    return update_job(job_id, job)


@router.delete("/{job_id}")
def remove_job(job_id: int):
    return delete_job(job_id)