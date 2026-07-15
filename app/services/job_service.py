from app.schemas.job import JobCreate


def create_job(job: JobCreate):
    return {
        "status": "success",
        "job": job.model_dump()
    }