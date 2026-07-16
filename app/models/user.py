from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.database.base import Base


class User(Base):

    __tablename__ = "users"
    
    resumes = relationship( 
    "Resume",
    back_populates="user",
    cascade="all, delete-orphan",
)

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False, index=True)

    phone = Column(String, unique=True)

    password = Column(String, nullable=False)
company_memberships = relationship(
    "CompanyMember",
    back_populates="user",
    cascade="all, delete-orphan",
)
    role = Column(String, default="candidate")

    is_active = Column(Boolean, default=True)

    jobs = relationship(
        "Job",
        back_populates="owner"
    )