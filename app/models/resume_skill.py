from sqlalchemy import (
    Boolean,
    Column,
    Date,
    ForeignKey,
    Integer,
)
from sqlalchemy.orm import relationship

from app.database.base import Base


class ResumeSkill(Base):
    __tablename__ = "resume_skills"

    resume_id = Column(
        Integer,
        ForeignKey("resumes.id"),
        primary_key=True,
        nullable=False,
    )

    skill_id = Column(
        Integer,
        ForeignKey("skills.id"),
        primary_key=True,
        nullable=False,
    )

    level = Column(
        Integer,
        nullable=False,
        default=1,
    )

    years_of_experience = Column(
        Integer,
        nullable=False,
        default=0,
    )

    last_used = Column(
        Date,
        nullable=True,
    )

    is_primary = Column(
        Boolean,
        nullable=False,
        default=False,
    )

    resume = relationship(
        "Resume",
        back_populates="skills",
    )

    skill = relationship(
        "Skill",
        back_populates="resumes",
    )