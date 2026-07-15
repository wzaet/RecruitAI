from app.database.session import SessionLocal
from app.models.job import Job
from app.schemas.job import JobCreate, JobUpdate


def create_job(job: JobCreate):
    db = SessionLocal()

    try:
        new_job = Job(
            title=job.title,
            department=job.department,
            location=job.location,
            employment_type=job.employment_type,
            salary_min=job.salary_min,
            salary_max=job.salary_max,
            experience=job.experience,
            education=job.education,
            description=job.description,
            deadline=job.deadline,
        )

        db.add(new_job)
        db.commit()
        db.refresh(new_job)

        return {
            "id": new_job.id,
            "message": "Job created successfully"
        }

    finally:
        db.close()


def get_jobs():
    db = SessionLocal()

    try:
        jobs = db.query(Job).all()
        return jobs

    finally:
        db.close()
        def update_job(job_id: int, job: JobUpdate):
    db = SessionLocal()

    try:
        existing_job = db.query(Job).filter(Job.id == job_id).first()

        if not existing_job:
            return {"error": "Job not found"}

        for key, value in job.model_dump().items():
            setattr(existing_job, key, value)

        db.commit()
        db.refresh(existing_job)

        return existing_job

    finally:
        db.close()
        def delete_job(job_id: int):
    db = SessionLocal()

    try:
        job = db.query(Job).filter(Job.id == job_id).first()

        if not job:
            return {"error": "Job not found"}

        db.delete(job)
        db.commit()

        return {"message": "Job deleted successfully"}

    finally:
        db.close()