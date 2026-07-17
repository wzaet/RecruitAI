from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.constants.field_lengths import NAME_LENGTH
from app.database.base import Base


class Language(Base):
    __tablename__ = "languages"

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
            name="fk_languages_resume",
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

    proficiency = Column(
        String(NAME_LENGTH),
        nullable=False,
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
        back_populates="languages",
    )