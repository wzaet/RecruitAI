from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Text,
)

from sqlalchemy.orm import relationship

from app.database.base import Base


class Applicant(Base):

    __tablename__ = "applicants"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)

    email = Column(String, unique=True)

    phone = Column(String)

    resume_path = Column(String)

    resume_text = Column(Text)

    skills = Column(Text)

    experience = Column(Text)

    education = Column(Text)

    languages = Column(Text)

    summary = Column(Text)

    job_id = Column(
        Integer,
        ForeignKey("jobs.id")
    )

    job = relationship(
        "Job",
        back_populates="applicants"
    )