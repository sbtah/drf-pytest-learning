import pytest
from django.urls import reverse
from rest_framework import status


LIST_STUDENT_URL = reverse('api:list-students')


class TestStudentApiViews():
    """Test cases for Student API Views."""
    pass


def test_student_list_api_view_url(client_drf, db):
    """Test that StudentListApiView url is responding."""

    response = client_drf.get(LIST_STUDENT_URL)
    assert response.status_code == status.HTTP_200_OK
