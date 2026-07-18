from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import (
    ProjectCreate,
    ProjectUpdate,
)
from app.services.base_service import BaseService


class ProjectService(BaseService[Project]):
    def __init__(self) -> None:
        super().__init__(Project)

    def get_by_resume(
        self,
        db: Session,
        resume_id: int,
    ) -> list[Project]:
        statement = select(Project).where(
            Project.resume_id == resume_id,
        )

        return list(
            db.scalars(statement).all(),
        )

    def create_project(
        self,
        db: Session,
        project_data: ProjectCreate,
    ) -> Project:
        project = Project(
            **project_data.model_dump(),
        )

        return self.create(
            db=db,
            obj=project,
        )

    def update_project(
        self,
        db: Session,
        project: Project,
        project_data: ProjectUpdate,
    ) -> Project:
        update_data = project_data.model_dump(
            exclude_unset=True,
        )

        for field, value in update_data.items():
            setattr(
                project,
                field,
                value,
            )

        return self.update(
            db=db,
            obj=project,
        )


project_service = ProjectService()