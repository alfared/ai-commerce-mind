from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ai_commerce_mind.db.base import BaseModel

if TYPE_CHECKING:
    from ai_commerce_mind.modules.store.models import Store


class Category(BaseModel):
    __tablename__ = "categories"

    __table_args__ = (
        UniqueConstraint(
            "store_id",
            "slug",
            name="uq_categories_store_id_slug",
        ),
    )

    store_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            "stores.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    slug: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    store: Mapped[Store] = relationship(
        back_populates="categories",
    )
