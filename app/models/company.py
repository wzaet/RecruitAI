from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.base import Base


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(200), nullable=False)

    slug = Column(String(200), unique=True, nullable=False)

    description = Column(Text)

    industry = Column(String(100))

    company_size = Column(String(50))

    website = Column(String(255))

    email = Column(String(255))

    phone = Column(String(50))

    country = Column(String(100))

    city = Column(String(100))

    address = Column(String(255))

    logo_url = Column(String(255))

    is_verified = Column(Boolean, default=False)

    is_active = Column(Boolean, default=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    jobs = relationship(
        "Job",
        back_populates="company",
        cascade="all, delete-orphan"
    )

    members = relationship(
        "CompanyMember",
        back_populates="company",
        cascade="all, delete-orphan"
    )