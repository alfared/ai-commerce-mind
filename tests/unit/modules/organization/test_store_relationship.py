from ai_commerce_mind.modules.organization.models import Organization
from ai_commerce_mind.modules.store.models import Store


def test_organization_can_own_store() -> None:
    organization = Organization(name="Test Organization", slug="test-organization")
    store = Store(
        name="Main Store",
        slug="main",
        currency="EUR",
        timezone="Europe/Prague",
    )

    organization.stores.append(store)

    assert organization.stores == [store]
    assert store.organization is organization
