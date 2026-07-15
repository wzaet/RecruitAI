from app.database.session import SessionLocal
from app.models.job import Job
from app.schemas.job import JobCreate


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