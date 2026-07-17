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

    # ==========================
    # Composite Primary Key
    # ==========================

    resume_id = Column(
        Integer,
        ForeignKey(
            "resumes.id",
            name="fk_resume_skills_resume",
            ondelete="CASCADE",
        ),
        primary_key=True,
        nullable=False,
    )

    skill_id = Column(
        Integer,
        ForeignKey(
            "skills.id",
            name="fk_resume_skills_skill",
            ondelete="CASCADE",
        ),
        primary_key=True,
        nullable=False,
    )

    # ==========================
    # Business Fields
    # ==========================

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

    # ==========================
    # Relationships
    # ==========================

    resume = relationship(
        "Resume",
        back_populates="skills",
    )

    skill = relationship(
        "Skill",
        back_populates="resumes",
    )