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

from app.database.base import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    title = Column(
        String(150),
        nullable=False,
    )

    summary = Column(
        Text,
    )

    current_position = Column(
        String(150),
    )

    current_company = Column(
        String(150),
    )

    years_of_experience = Column(
        Integer,
        nullable=False,
        default=0,
    )

    city = Column(
        String(100),
    )

    country = Column(
        String(100),
    )

    resume_file = Column(
        String(255),
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

    user = relationship(
        "User",
        back_populates="resumes",
    )

    skills = relationship(
        "ResumeSkill",
        back_populates="resume",
        cascade="all, delete-orphan",
    )