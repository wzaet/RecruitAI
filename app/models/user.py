from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.database.base import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False, index=True)

    phone = Column(String, unique=True)

    password = Column(String, nullable=False)

    role = Column(String, default="candidate")

    is_active = Column(Boolean, default=True)

    jobs = relationship(
        "Job",
        back_populates="owner"
    )