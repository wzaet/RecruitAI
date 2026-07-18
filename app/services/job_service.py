from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.job import Job
from app.schemas.job import (
    JobCreate,
    JobUpdate,
)
from app.services.base_service import BaseService


class JobService(BaseService[Job]):
    def __init__(self) -> None:
        super().__init__(Job)

    def get_by_company(
        self,
        db: Session,
        company_id: int,
    ) -> list[Job]:
        statement = select(Job).where(
            Job.company_id == company_id,
        )

        return list(
            db.scalars(statement).all(),
        )

    def get_active_jobs(
        self,
        db: Session,
    ) -> list[Job]:
        statement = select(Job).where(
            Job.is_active.is_(True),
        )

        return list(
            db.scalars(statement).all(),
        )

    def create_job(
        self,
        db: Session,
        job_data: JobCreate,
    ) -> Job:
        job = Job(
            **job_data.model_dump(),
        )

        return self.create(
            db=db,
            obj=job,
        )

    def update_job(
        self,
        db: Session,
        job: Job,
        job_data: JobUpdate,
    ) -> Job:
        update_data = job_data.model_dump(
            exclude_unset=True,
        )

        for field, value in update_data.items():
            setattr(
                job,
                field,
                value,
            )

        return self.update(
            db=db,
            obj=job,
        )

    def activate(
        self,
        db: Session,
        job: Job,
    ) -> Job:
        job.is_active = True

        return self.update(
            db=db,
            obj=job,
        )

    def deactivate(
        self,
        db: Session,
        job: Job,
    ) -> Job:
        job.is_active = False

        return self.update(
            db=db,
            obj=job,
        )


job_service = JobService()