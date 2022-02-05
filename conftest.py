import pytest


@pytest.fixture()
def client_drf():
    """A DRF test client instance."""

    from rest_framework.test import APIClient

    return APIClient()
