from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.constants.field_lengths import (
    SHORT_TEXT_LENGTH,
)
from app.database.base import Base


class CompanyMember(Base):
    __tablename__ = "company_members"

    __table_args__ = (
        UniqueConstraint(
            "company_id",
            "user_id",
            name="uq_company_member",
        ),
    )

    # ==========================
    # Primary Key
    # ==========================

    id = Column(Integer, primary_key=True, index=True)

    # ==========================
    # Foreign Keys
    # ==========================

    company_id = Column(
        Integer,
        ForeignKey(
            "companies.id",
            name="fk_company_members_company",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    user_id = Column(
        Integer,
        ForeignKey(
            "users.id",
            name="fk_company_members_user",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    # ==========================
    # Business Fields
    # ==========================

    role = Column(
        String(SHORT_TEXT_LENGTH),
        nullable=False,
        default="RECRUITER",
    )

    is_active = Column(
        Boolean,
        nullable=False,
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

    company = relationship(
        "Company",
        back_populates="members",
    )

    user = relationship(
        "User",
        back_populates="company_memberships",
    )