from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.constants.field_lengths import (
    EMAIL_LENGTH,
    NAME_LENGTH,
    PASSWORD_LENGTH,
    PHONE_LENGTH,
    ROLE_LENGTH,
)
from app.database.base import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = ()

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

    full_name = Column(
        String(NAME_LENGTH),
        nullable=False,
    )

    email = Column(
        String(EMAIL_LENGTH),
        unique=True,
        nullable=False,
        index=True,
    )

    phone = Column(
        String(PHONE_LENGTH),
        unique=True,
    )

    password = Column(
        String(PASSWORD_LENGTH),
        nullable=False,
    )

    role = Column(
        String(ROLE_LENGTH),
        default="candidate",
    )

    is_active = Column(
        Boolean,
        default=True,
    )

    # ==========================
    # Relationships
    # ==========================

    resumes = relationship(
        "Resume",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    jobs = relationship(
        "Job",
        back_populates="owner",
    )

    company_memberships = relationship(
        "CompanyMember",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    applications = relationship(
        "Application",
        back_populates="user",
        cascade="all, delete-orphan",
    )