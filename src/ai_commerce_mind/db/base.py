from typing import Final

from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

from ai_commerce_mind.db.mixins import TimestampMixin, UUIDPrimaryKeyMixin

NAMING_CONVENTION: Final[dict[str, str]] = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(
    naming_convention=NAMING_CONVENTION,
)


class Base(DeclarativeBase):
    metadata = metadata


class BaseModel(
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    Base,
):
    __abstract__ = True
