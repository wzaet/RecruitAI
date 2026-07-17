from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.constants.field_lengths import (
    NAME_LENGTH,
    URL_LENGTH,
)
from app.database.base import Base


class Project(Base):
    __tablename__ = "projects"

    # ==========================
    # Primary Key
    # ==========================

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # ==========================
    # Foreign Keys
    # ==========================

    resume_id = Column(
        Integer,
        ForeignKey(
            "resumes.id",
            name="fk_projects_resume",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    # ==========================
    # Business Fields
    # ==========================

    name = Column(
        String(NAME_LENGTH),
        nullable=False,
    )

    role = Column(
        String(NAME_LENGTH),
    )

    organization = Column(
        String(NAME_LENGTH),
    )

    description = Column(
        Text,
    )

    project_url = Column(
        String(URL_LENGTH),
    )

    repository_url = Column(
        String(URL_LENGTH),
    )

    start_date = Column(
        Date,
    )

    end_date = Column(
        Date,
    )

    is_ongoing = Column(
        Boolean,
        nullable=False,
        default=False,
    )

    display_order = Column(
        Integer,
        nullable=False,
        default=0,
    )

    # ==========================
    # Audit Fields
    # ==========================

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    # ==========================
    # Relationships
    # ==========================

    resume = relationship(
        "Resume",
        back_populates="projects",
    )