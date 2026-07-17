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
    LOCATION_LENGTH,
    NAME_LENGTH,
)
from app.database.base import Base


class Education(Base):
    __tablename__ = "educations"

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
            name="fk_educations_resume",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    # ==========================
    # Business Fields
    # ==========================

    institution_name = Column(
        String(NAME_LENGTH),
        nullable=False,
    )

    degree = Column(
        String(NAME_LENGTH),
        nullable=False,
    )

    field_of_study = Column(
        String(NAME_LENGTH),
    )

    location = Column(
        String(LOCATION_LENGTH),
    )

    start_date = Column(
        Date,
        nullable=False,
    )

    end_date = Column(
        Date,
    )

    is_current = Column(
        Boolean,
        nullable=False,
        default=False,
    )

    grade = Column(
        String(NAME_LENGTH),
    )

    description = Column(
        Text,
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
        back_populates="educations",
    )