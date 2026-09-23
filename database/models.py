from datetime import date
from sqlalchemy import Date, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from .db import Base


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )
    last_name: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )
    email: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )
    phone: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )
    birth_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )
    additional_data: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )
