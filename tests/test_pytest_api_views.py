import pytest
from django.urls import reverse
from rest_framework import status
from mixer.backend.django import mixer
from classroom.models import Student
from api.serializers import StudentSerializer


# Endpoints tested.
LIST_STUDENT_URL = reverse('api:list-students')


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

        student = mixer.blend(Student, first_name='Tester 2')
        students = Student.objects.all()
        response = client_drf.get(LIST_STUDENT_URL)
        serializer = StudentSerializer(students, many=True)
        assert response.data == serializer.data

    # StudentDetailAPiView Tests.
