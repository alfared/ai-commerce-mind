from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ai_commerce_mind.db.base import BaseModel

if TYPE_CHECKING:
    from ai_commerce_mind.modules.category.models import Category
    from ai_commerce_mind.modules.organization.models import Organization


class Store(BaseModel):
    __tablename__ = "stores"
    __table_args__ = (
        UniqueConstraint("organization_id", "slug", name="uq_store_organization_id_slug"),
    )

    organization_id: Mapped[UUID] = mapped_column(
        ForeignKey(
            "organizations.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(String(255), nullable=False)

    slug: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    currency: Mapped[str] = mapped_column(
        String(3),
        nullable=False,
        default="EUR",
    )

    timezone: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        default="UTC",
    )

    organization: Mapped[Organization] = relationship(
        back_populates="stores",
    )

    categories: Mapped[list[Category]] = relationship(
        back_populates="store",
        cascade="all, delete-orphan",
    )
