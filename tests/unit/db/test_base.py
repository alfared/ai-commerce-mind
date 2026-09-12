from ai_commerce_mind.db.base import NAMING_CONVENTION, Base


def test_base_has_naming_convention() -> None:
    assert Base.metadata.naming_convention == NAMING_CONVENTION


def test_primary_key_naming_convention() -> None:
    assert NAMING_CONVENTION["pk"] == "pk_%(table_name)s"


def test_foreign_key_naming_convention() -> None:
    assert NAMING_CONVENTION["fk"] == "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"
