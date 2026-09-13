import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from ai_commerce_mind.modules.organization.models import Organization
from ai_commerce_mind.modules.store.models import Store


async def test_store_belongs_to_organization(db_session: AsyncSession) -> None:
    organization = Organization(
        name="Acme Commerce",
        slug="acme-commerce",
    )

    store = Store(
        name="Main Store",
        slug="main",
        currency="EUR",
        timezone="Europe/Prague",
        organization=organization,
    )

    db_session.add(organization)
    await db_session.flush()

    assert organization.id is not None
    assert store.id is not None
    assert store.organization_id == organization.id
    assert store.organization is organization


async def test_store_slug_must_be_unique_within_organizations(
    db_session: AsyncSession,
) -> None:
    organization = Organization(
        name="Acme Commerce",
        slug="acme-commerce",
    )

    first_store = Store(
        name="Main Store",
        slug="main",
        currency="EUR",
        timezone="Europe/Prague",
        organization=organization,
    )

    second_store = Store(
        name="Secondary Store",
        slug="main",
        currency="EUR",
        timezone="Europe/Prague",
        organization=organization,
    )

    db_session.add_all(
        [
            organization,
            first_store,
            second_store,
        ]
    )

    with pytest.raises(IntegrityError):
        await db_session.commit()


async def test_same_store_slug_is_allowed_in_different_organizations(
    db_session: AsyncSession,
) -> None:
    first_organization = Organization(
        name="Acme A",
        slug="acme-a",
    )

    second_organization = Organization(
        name="Globex",
        slug="globex",
    )

    first_store = Store(
        name="Main Store",
        slug="main",
        currency="EUR",
        timezone="Europe/Prague",
        organization=first_organization,
    )

    second_store = Store(
        name="Main Store",
        slug="main",
        currency="EUR",
        timezone="Europe/Prague",
        organization=second_organization,
    )

    db_session.add_all(
        [
            first_organization,
            second_organization,
        ]
    )

    await db_session.commit()

    assert first_store.organization_id != second_store.organization_id
    assert first_store.organization is not second_store.organization
    assert first_store.slug == second_store.slug
