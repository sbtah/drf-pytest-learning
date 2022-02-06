import pytest


@pytest.fixture()
def client_drf():
    """A DRF test client instance."""

    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def student_data():
    return {
        'first_name': 'test',
        'last_name': 'tester',
        'user_number': '10565',
    }
