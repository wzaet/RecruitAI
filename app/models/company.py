from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.constants.field_lengths import (
    EMAIL_LENGTH,
    LOCATION_LENGTH,
    LONG_TEXT_LENGTH,
    NAME_LENGTH,
    PHONE_LENGTH,
    SLUG_LENGTH,
    URL_LENGTH,
)
from app.database.base import Base


class Company(Base):
    __tablename__ = "companies"

    # ==========================
    # Primary Key
    # ==========================

    id = Column(Integer, primary_key=True, index=True)

    # ==========================
    # Business Fields
    # ==========================

    name = Column(
        String(NAME_LENGTH),
        nullable=False,
    )

    slug = Column(
        String(SLUG_LENGTH),
        unique=True,
        nullable=False,
    )

    description = Column(Text)

    industry = Column(String(NAME_LENGTH))

    company_size = Column(String(LONG_TEXT_LENGTH))

    website = Column(String(URL_LENGTH))

    email = Column(String(EMAIL_LENGTH))

    phone = Column(String(PHONE_LENGTH))

    country = Column(String(LOCATION_LENGTH))

    city = Column(String(LOCATION_LENGTH))

    address = Column(String(LOCATION_LENGTH))

    logo_url = Column(String(URL_LENGTH))

    is_verified = Column(
        Boolean,
        default=False,
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    # ==========================
    # Audit Fields
    # ==========================

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    # ==========================
    # Relationships
    # ==========================

    jobs = relationship(
        "Job",
        back_populates="company",
        cascade="all, delete-orphan",
    )

    members = relationship(
        "CompanyMember",
        back_populates="company",
        cascade="all, delete-orphan",
    )

    experiences = relationship(
        "Experience",
        back_populates="company",
    )