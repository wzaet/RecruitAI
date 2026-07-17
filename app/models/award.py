from sqlalchemy import (
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.constants.field_lengths import (
    NAME_LENGTH,
    URL_LENGTH,
)
from app.database.base import Base


class Award(Base):
    __tablename__ = "awards"

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
            name="fk_awards_resume",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    # ==========================
    # Business Fields
    # ==========================

    title = Column(
        String(NAME_LENGTH),
        nullable=False,
    )

    issuer = Column(
        String(NAME_LENGTH),
    )

    award_date = Column(
        Date,
    )

    description = Column(
        Text,
    )

    award_url = Column(
        String(URL_LENGTH),
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
        back_populates="awards",
    )