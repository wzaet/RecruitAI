from sqlalchemy.orm import Session

from app.models.application import Application
from app.schemas.application import (
    ApplicationCreate,
    ApplicationUpdate,
)
from app.services.base_service import BaseService


class ApplicationService(BaseService[Application]):
    def __init__(self) -> None:
        super().__init__(Application)

    def create_application(
        self,
        db: Session,
        application_data: ApplicationCreate,
    ) -> Application:
        application = Application(
            **application_data.model_dump(),
        )

        return self.create(
            db=db,
            obj=application,
        )

    def update_application(
        self,
        db: Session,
        application: Application,
        application_data: ApplicationUpdate,
    ) -> Application:
        update_data = application_data.model_dump(
            exclude_unset=True,
        )

        for field, value in update_data.items():
            setattr(
                application,
                field,
                value,
            )

        return self.update(
            db=db,
            obj=application,
        )


application_service = ApplicationService()