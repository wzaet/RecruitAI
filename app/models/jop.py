from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.database.base import Base


class Job(Base):

    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(200), nullable=False)

    department = Column(String(100))

    location = Column(String(100))

    employment_type = Column(String(50))

    salary_min = Column(Integer)

    salary_max = Column(Integer)

    experience = Column(String(100))

    education = Column(String(200))

    description = Column(String)

    deadline = Column(String)

    status = Column(String(20), default="Open")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )