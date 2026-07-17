from sqlalchemy import (
    Boolean,
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
    LOCATION_LENGTH,
    NAME_LENGTH,
    URL_LENGTH,
)
from app.database.base import Base


class Resume(Base):
    __tablename__ = "resumes"

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
            name="fk_resumes_user",
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

    summary = Column(Text)

    current_position = Column(
        String(NAME_LENGTH),
    )

    current_company = Column(
        String(NAME_LENGTH),
    )

    years_of_experience = Column(
        Integer,
        nullable=False,
        default=0,
    )

    city = Column(
        String(LOCATION_LENGTH),
    )

    country = Column(
        String(LOCATION_LENGTH),
    )

    resume_file = Column(
        String(URL_LENGTH),
    )

    parsed = Column(
        Boolean,
        nullable=False,
        default=False,
    )

    is_public = Column(
        Boolean,
        nullable=False,
        default=True,
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
        back_populates="resumes",
    )

    skills = relationship(
        "ResumeSkill",
        back_populates="resume",
        cascade="all, delete-orphan",
    )