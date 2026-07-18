from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.constants.field_lengths import (
    NAME_LENGTH,
    URL_LENGTH,
)
from app.database.base import Base


class Certificate(Base):
    __tablename__ = "certificates"

    # ==========================
    # Primary Key
    # ==========================

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    # ==========================
    # Foreign Keys
    # ==========================

    resume_id = Column(
        Integer,
        ForeignKey(
            "resumes.id",
            name="fk_certificates_resume",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    # ==========================
    # Business Fields
    # ==========================

    name = Column(
        String(NAME_LENGTH),
        nullable=False,
    )

    issuing_organization = Column(
        String(NAME_LENGTH),
        nullable=False,
    )

    issue_date = Column(
        Date,
    )

    expiration_date = Column(
        Date,
    )

    credential_id = Column(
        String(NAME_LENGTH),
    )

    credential_url = Column(
        String(URL_LENGTH),
    )

    does_not_expire = Column(
        Boolean,
        nullable=False,
        default=False,
    )

    display_order = Column(
        Integer,
        nullable=False,
        default=0,
    )

    # ==========================
    # Audit Fields
    # ==========================

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    # ==========================
    # Relationships
    # ==========================

    resume = relationship(
        "Resume",
        back_populates="certificates",
    )