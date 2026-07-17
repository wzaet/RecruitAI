from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.constants.field_lengths import (
    NAME_LENGTH,
)
from app.database.base import Base


class Skill(Base):
    __tablename__ = "skills"

    # ==========================
    # Primary Key
    # ==========================

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # ==========================
    # Business Fields
    # ==========================

    name = Column(
        String(NAME_LENGTH),
        unique=True,
        nullable=False,
        index=True,
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

    resumes = relationship(
        "ResumeSkill",
        back_populates="skill",
        cascade="all, delete-orphan",
    )