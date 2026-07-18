from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.resume_link import ResumeLink
from app.schemas.resume_link import ResumeLinkCreate, ResumeLinkUpdate
from app.services.base_service import BaseService


class ResumeLinkService(BaseService[ResumeLink]):
    def __init__(self) -> None:
        super().__init__(ResumeLink)

    def get_by_resume(
        self,
        db: Session,
        resume_id: int,
    ) -> list[ResumeLink]:
        statement = select(ResumeLink).where(
            ResumeLink.resume_id == resume_id,
        )

        return list(db.scalars(statement))

    def create_resume_link(
        self,
        db: Session,
        link_data: ResumeLinkCreate,
    ) -> ResumeLink:
        link = ResumeLink(**link_data.model_dump())
        return self.create(db=db, obj=link)

    def update_resume_link(
        self,
        db: Session,
        link: ResumeLink,
        link_data: ResumeLinkUpdate,
    ) -> ResumeLink:
        update_data = link_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(link, field, value)

        return self.update(db=db, obj=link)


resume_link_service = ResumeLinkService()