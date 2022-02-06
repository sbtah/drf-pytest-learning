from email.policy import HTTP
import json
import pytest
from django.urls import reverse
from rest_framework import status
from mixer.backend.django import mixer
from classroom.models import Student
from api.serializers import StudentSerializer


# Endpoints
LIST_STUDENT_URL = reverse('api:student-list')
CREATE_STUDENT_URL = reverse('api:student-create')


class TestStudentApiViews():
    """Test cases for Student API Views."""

    # StudentListAPiView Tests.
    def test_student_list_api_view_url(self, client_drf, db):
        """Test that StudentListApiView url is responding."""

        response = client_drf.get(LIST_STUDENT_URL)
        assert response.status_code == status.HTTP_200_OK

    def test_student_list_api_view_lists_data(self, client_drf, db):
        """Test that StudentListApiView url is listing proper data."""

        student = mixer.blend(Student, first_name='Tester')
        response = client_drf.get(LIST_STUDENT_URL)
        assert response.data[0]['first_name'] == 'Tester'
        assert len(response.data) == 1

    def test_student_list_api_view_serialize_data(self, client_drf, db):
        """Test that data returned from url is properly serialized."""

        student = mixer.blend(Student, first_name='Tester')
        students = Student.objects.all()
        response = client_drf.get(LIST_STUDENT_URL)
        serializer = StudentSerializer(students, many=True)
        assert response.data == serializer.data

    # StudentCreateAPiView Tests.
    def test_student_create_api_view_url(self, client_drf, db):
        """Test url response of StudentCreateApiView in no data given."""

        response = client_drf.post(CREATE_STUDENT_URL)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_student_create_api_creates_data(self, client_drf, student_data, db):
        """Test that Student object is created at related endpoint."""
        # data is provided by the fixture in conftest.
        response = client_drf.post(
            CREATE_STUDENT_URL, data=student_data, follow=True)
        assert response.status_code == status.HTTP_201_CREATED
