from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.base import Base


class Application(Base):
    __tablename__ = "applications"

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

    user_id = Column(
        Integer,
        ForeignKey(
            "users.id",
            name="fk_applications_user",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    job_id = Column(
        Integer,
        ForeignKey(
            "jobs.id",
            name="fk_applications_job",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    resume_id = Column(
        Integer,
        ForeignKey(
            "resumes.id",
            name="fk_applications_resume",
            ondelete="SET NULL",
        ),
        nullable=True,
        index=True,
    )

    # ==========================
    # Business Fields
    # ==========================

    status = Column(
        Integer,
        nullable=False,
        default=1,
    )

    cover_letter = Column(
        Text,
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

    user = relationship(
        "User",
        back_populates="applications",
    )

    job = relationship(
        "Job",
        back_populates="applications",
    )

    resume = relationship(
        "Resume",
        back_populates="applications",
    )