from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ai_commerce_mind.db.base import BaseModel

if TYPE_CHECKING:
    from ai_commerce_mind.modules.store.models import Store


class Organization(BaseModel):
    __tablename__ = "organizations"

    name: Mapped[str] = mapped_column(String(255), nullable=False)

    slug: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
        index=True,
    )

    stores: Mapped[list[Store]] = relationship(
        back_populates="organization",
        cascade="all, delete-orphan",
    )
