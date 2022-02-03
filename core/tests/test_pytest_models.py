from classroom.models import Classroom, Student
from mixer.backend.django import mixer
import pytest
pytestmark = pytest.mark.django_db


class TestStudentModel():
    """Tests for Student object."""

    def test_student_can_be_created(self):
        """Test that Student object can be created."""

        student1 = mixer.blend(Student, first_name='test')
        assert Student.objects.all().count() == 1
        assert student1.first_name == 'test'

    def test_str_of_student(self):
        """Test __str__ of Student model."""

        student1 = mixer.blend(Student, first_name='test', last_name='test')
        assert str(student1) == 'test test'

    def test_grade_fail(self):
        """Test get_grade returns proper data
        (average_score < 40) -> 'Fail'
        """

        student1 = mixer.blend(Student, average_score=33)
        assert student1.get_grade() == 'Fail'

    def test_grade_pass(self):
        """Test get_grade returns proper data
        (average_score < 70 and average_score > 40) -> 'Pass'
        """

        student1 = mixer.blend(Student, average_score=66)
        assert student1.get_grade() == 'Pass'

    def test_grade_excellent(self):
        """Test get_grade returns proper data
        (average_score < 100 and average_score > 70) -> 'Excellent'
        """

        student1 = mixer.blend(Student, average_score=86)
        assert student1.get_grade() == 'Excellent'

    def test_grade_error(self):
        """Test get_grade returns proper data
        (average_score > 100) -> 'Error'
        """

        student1 = mixer.blend(Student, average_score=101)
        assert student1.get_grade() == 'Error'


class TestClassroomModel():
    """Tests for Classroom object."""

    def test_classroom_create(self):
        """Test creation of Classroom object."""

        classroom = mixer.blend(Classroom, name='Physics')
        assert Classroom.objects.all().count() == 1
        assert classroom.name == 'Physics'

    def test_classroom_str(self):
        """Test __str__ of Classroom object."""

        classroom = mixer.blend(Classroom, name='test classroom')
        assert str(classroom) == 'test classroom'
