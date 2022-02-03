from django.core.exceptions import ValidationError
from classroom.models import Classroom, Student, average_grade_validator, name_validator
from mixer.backend.django import mixer
import pytest
pytestmark = pytest.mark.django_db


def test_average_grade_validator():
    """Test that average grade that is lower then 0 raises an error."""

    with pytest.raises(ValidationError) as error:
        average_grade_validator(-2.0)


def test_name_validator():
    """Test that bad characters used for first_name or last_namer raises errors."""

    with pytest.raises(ValidationError) as error:
        name_validator('a')

    with pytest.raises(ValidationError) as error:
        name_validator('12312')


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

    @pytest.mark.parametrize('failed', [float(num) for num in range(0, 40)])
    def test_grade_fail(self, failed):
        """Test get_grade returns proper data
        (average_score < 40) -> 'Fail'
        """

        student1 = mixer.blend(Student, average_score=failed)
        assert student1.get_grade() == 'Fail'

    @pytest.mark.parametrize('passed', [float(num) for num in range(40, 70)])
    def test_grade_pass(self, passed):
        """Test get_grade returns proper data
        (average_score < 70 and average_score > 40) -> 'Pass'
        """

        student1 = mixer.blend(Student, average_score=passed)
        assert student1.get_grade() == 'Pass'

    @pytest.mark.parametrize('excellent', [float(num) for num in range(70, 100)])
    def test_grade_excellent(self, excellent):
        """Test get_grade returns proper data
        (average_score < 100 and average_score > 70) -> 'Excellent'
        """

        student1 = mixer.blend(Student, average_score=excellent)
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
