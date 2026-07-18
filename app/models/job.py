from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.constants.field_lengths import (
    MEDIUM_TEXT_LENGTH,
    NAME_LENGTH,
    SHORT_TEXT_LENGTH,
)
from app.database.base import Base


class Job(Base):
    __tablename__ = "jobs"

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

    owner_id = Column(
        Integer,
        ForeignKey(
            "users.id",
            name="fk_jobs_owner",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    company_id = Column(
        Integer,
        ForeignKey(
            "companies.id",
            name="fk_jobs_company",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    # ==========================
    # Business Fields
    # ==========================

    title = Column(
        String(NAME_LENGTH),
        nullable=False,
    )

    department = Column(
        String(MEDIUM_TEXT_LENGTH),
    )

    location = Column(
        String(MEDIUM_TEXT_LENGTH),
    )

    employment_type = Column(
        String(SHORT_TEXT_LENGTH),
    )

    salary_min = Column(
        Integer,
    )

    salary_max = Column(
        Integer,
    )

    experience = Column(
        String(MEDIUM_TEXT_LENGTH),
    )

    education = Column(
        String(NAME_LENGTH),
    )

    description = Column(
        Text,
    )

    deadline = Column(
        String(SHORT_TEXT_LENGTH),
    )

    status = Column(
        String(SHORT_TEXT_LENGTH),
        nullable=False,
        default="Open",
    )

    # ==========================
    # Audit Fields
    # ==========================

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # ==========================
    # Relationships
    # ==========================

    owner = relationship(
        "User",
        back_populates="jobs",
    )

    company = relationship(
        "Company",
        back_populates="jobs",
    )

    applications = relationship(
        "Application",
        back_populates="job",
        cascade="all, delete-orphan",
    )