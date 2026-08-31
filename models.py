
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from db import Base


# =========================
# USER MODEL
# =========================

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False
    )

    password = Column(
        String(255),
        nullable=False
    )

    # Relationship with reports
    reports = relationship(
        "Report",
        back_populates="user",
        cascade="all, delete-orphan"
    )


# =========================
# REPORT MODEL
# =========================

class Report(Base):

    __tablename__ = "reports"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    resume_text = Column(
        Text,
        nullable=False
    )

    result = Column(
        Text,
        nullable=False
    )

    # Relationship with user
    user = relationship(
        "User",
        back_populates="reports"
    )

