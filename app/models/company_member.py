from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    DateTime,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.base import Base


class CompanyMember(Base):
    __tablename__ = "company_members"

    id = Column(Integer, primary_key=True, index=True)

    company_id = Column(
        Integer,
        ForeignKey("companies.id"),
        nullable=False,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    role = Column(
        String(50),
        nullable=False,
        default="recruiter",
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    company = relationship(
        "Company",
        back_populates="members",
    )

    user = relationship(
        "User",
        back_populates="company_memberships",
    )