from django.urls import reverse
from rest_framework import status
from mixer.backend.django import mixer
from classroom.models import Student, Classroom
from api.serializers import StudentSerializer


# Endpoints
LIST_STUDENT_URL = reverse('api:student-list')
CREATE_STUDENT_URL = reverse('api:student-create')
LIST_CLASSROOM_URL = reverse('api:classroom-list')


class TestStudentApiViews():
    """Test cases for Student API Views."""

    # StudentListAPiView Tests.
    def test_student_list_api_view_url(self, client_drf, db):
        """Test that StudentListApiView url is responding."""

        response = client_drf.get(LIST_STUDENT_URL)
        assert response.data == []
        assert Student.objects.all().count() == 0
        assert response.status_code == status.HTTP_200_OK

    def test_student_list_api_view_lists_data(self, client_drf, db):
        """Test that StudentListApiView url is listing proper data."""

        student = mixer.blend(Student, first_name='Tester')
        response = client_drf.get(LIST_STUDENT_URL)

        assert response.data[0]['first_name'] == 'Tester'
        assert len(response.data) == 1
        assert Student.objects.all().count() == 1

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
        """Test that Student object is created and is_qualified is set to False."""
        # data is provided by the fixture student_data in conftest.
        response = client_drf.post(
            CREATE_STUDENT_URL, data=student_data, follow=True)
        user = Student.objects.get(id=1)
        assert response.status_code == status.HTTP_201_CREATED
        assert user.is_qualified == False

    def test_student_create_api_with_bad_data(self, client_drf, db):
        """Test that Student object is not created while data is wrong."""

        data = {
            'first_name': '',
            'last_name': 'tester',
            'user_number': '10565',
        }
        response = client_drf.post(
            CREATE_STUDENT_URL, data=data, follow=True)
        assert response.data['first_name'] != ''
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    # StudentDetailsAPiView Tests.
    def test_student_details_view_url(self, client_drf, db):
        """Test url response of StudentDetailsApiView."""

        student = mixer.blend(Student)
        response = client_drf.get(
            reverse('api:student-details', kwargs={'pk': student.id}))
        assert response.status_code == status.HTTP_200_OK

    def test_student_details_view_gets_data(self, client_drf, db):
        """Test that StudentDetailsView returns proper data."""

        student = mixer.blend(Student, first_name='Student')
        response = client_drf.get(
            reverse('api:student-details', kwargs={'pk': student.id}))
        assert response.data['first_name'] == 'Student'

    def test_student_details_response_if_no_data(self, client_drf, db):
        """Test that StudentDetailsView returns status 404 if Student does not exists."""

        response = client_drf.get(
            reverse('api:student-details', kwargs={'pk': 3}))
        assert response.data['detail'] == 'Not found.'
        assert response.status_code == status.HTTP_404_NOT_FOUND

    # StudentDeletesAPiView Tests.
    def test_student_delete_view(self, client_drf, db):
        """Test that data is deleted with StudentDeleteApiView."""

        student = mixer.blend(Student)
        assert Student.objects.all().count() == 1
        response = client_drf.delete(
            reverse('api:student-delete', kwargs={'pk': student.id}))
        assert Student.objects.all().count() == 0
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_student_delete_view_if_no_data(self, client_drf, db):
        """Test that StudentDeleteView returns status 404 if Student does not exists."""

        response = client_drf.delete(
            reverse('api:student-delete', kwargs={'pk': 3}))
        assert response.data['detail'] == 'Not found.'
        assert response.status_code == status.HTTP_404_NOT_FOUND


class TestClassroomApiViews():
    """Test cases for Classroom API Views."""

    # ClassroomListApiView.
    def test_classroom_list_api_view_url(self, client_drf, db):
        """Test reponse from url of ClassroomListApiView."""

        response = client_drf.get(LIST_CLASSROOM_URL)
        assert Classroom.objects.all().count() == 0
        assert response.status_code == status.HTTP_200_OK

    def test_classroom_api_view_lists_data(self, client_drf, db):
        """Test that ClassroomListApiView properly list data."""

        classroom = mixer.blend(Classroom, name='Physics')
        response = client_drf.get(LIST_CLASSROOM_URL)
        assert Classroom.objects.all().count() == 1
        assert response.data[0]['name'] == 'Physics'
        assert response.status_code == status.HTTP_200_OK

    def test_clasroom_api_view_serialize_data(self, client_drf, db):
        """Test that data listed by ClassroomListApiView is properly serialized."""
        pass

    # ClassroomStudentCapacityApiView
    def test_classroom_student_capacity_url(self, client_drf, db):
        """Test reponse from url of ClassroomStudentCapacityApiView."""

        response = client_drf.get(
            reverse('api:classroom-student-capacity',
                    kwargs={'student_capacity': 100}))
        assert Classroom.objects.all().count() == 0
        assert response.status_code == status.HTTP_200_OK

    def test_classroom_student_capacity_list_proper_data(self, client_drf, db):
        """Test that ClassroomStudentCapacityApiView is listing proper data."""

        classroom_0 = mixer.blend(
            Classroom, name='Chemistry', student_capacity=50)
        classroom_1 = mixer.blend(
            Classroom, name='Physics', student_capacity=100)
        classroom_2 = mixer.blend(
            Classroom, name='History', student_capacity=200)
        assert Classroom.objects.all().count() == 3
        response = client_drf.get(
            reverse('api:classroom-student-capacity',
                    kwargs={'student_capacity': 100}))
        assert response.status_code == status.HTTP_200_OK
        print(response.data)
        assert response.data[0]['name'] == 'Physics'
        assert response.data[1]['name'] == 'History'
        assert len(response.data) == 2

    def test_clasroom_student_capacity_view_serialize_data(self, client_drf, db):
        """Test that data listed by ClassroomStudentCapacityApiView is properly serialized."""
        pass
