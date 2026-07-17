from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.constants.field_lengths import (
    EMAIL_LENGTH,
    NAME_LENGTH,
    PHONE_LENGTH,
)
from app.database.base import Base


class Reference(Base):
    __tablename__ = "references"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    resume_id = Column(
        Integer,
        ForeignKey(
            "resumes.id",
            name="fk_references_resume",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    full_name = Column(
        String(NAME_LENGTH),
        nullable=False,
    )

    job_title = Column(
        String(NAME_LENGTH),
    )

    company = Column(
        String(NAME_LENGTH),
    )

    email = Column(
        String(EMAIL_LENGTH),
    )

    phone = Column(
        String(PHONE_LENGTH),
    )

    relationship_type = Column(
        String(NAME_LENGTH),
    )

    is_public = Column(
        Boolean,
        nullable=False,
        default=False,
    )

    display_order = Column(
        Integer,
        nullable=False,
        default=0,
    )

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

    resume = relationship(
        "Resume",
        back_populates="references",
    )