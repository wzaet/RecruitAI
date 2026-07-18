from sqlalchemy.orm import Session

from app.models.application import Application
from app.schemas.application import (
    ApplicationCreate,
    ApplicationUpdate,
)


class ApplicationService:

    def get(
        self,
        db: Session,
        obj_id: int,
    ):
        return (
            db.query(Application)
            .filter(Application.id == obj_id)
            .first()
        )

    def get_all(
        self,
        db: Session,
    ):
        return db.query(Application).all()

    def create_application(
        self,
        db: Session,
        application_data: ApplicationCreate,
    ):
        application = Application(
            **application_data.model_dump()
        )

        db.add(application)
        db.commit()
        db.refresh(application)

        return application

    def update_application(
        self,
        db: Session,
        application: Application,
        application_data: ApplicationUpdate,
    ):
        update_data = application_data.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                application,
                key,
                value,
            )

        db.commit()
        db.refresh(application)

        return application

    def delete(
        self,
        db: Session,
        obj: Application,
    ):
        db.delete(obj)
        db.commit()


application_service = ApplicationService()