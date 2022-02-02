from django.test import TestCase
from classroom.models import Classroom, Student
from mixer.backend.django import mixer
import pytest
pytestmark = pytest.mark.django_db


def test_student_can_be_created():
    """Test that Student object can be created."""

    student1 = mixer.blend(Student, first_name='test')
    assert student1.first_name == 'test'


def test_str_of_student():
    """Test __str__ of Student model."""

    student1 = mixer.blend(Student, first_name='test', last_name='test')
    assert str(student1) == 'test test'


def test_grade_fail():
    """Test get_grade returns proper data
    (average_score < 40) -> 'Fail'
    """

    student1 = mixer.blend(Student, average_score=33)
    assert student1.get_grade() == 'Fail'


def test_grade_pass():
    """Test get_grade returns proper data
    (average_score < 70 and average_score > 40) -> 'Pass'
    """

    student1 = mixer.blend(Student, average_score=66)
    assert student1.get_grade() == 'Pass'


def test_grade_excellent():
    """Test get_grade returns proper data
    (average_score < 100 and average_score > 70) -> 'Excellent'
    """

    student1 = mixer.blend(Student, average_score=86)
    assert student1.get_grade() == 'Excellent'


def test_grade_error():
    """Test get_grade returns proper data
    (average_score > 100) -> 'Error'
    """

    student1 = mixer.blend(Student, average_score=101)
    assert student1.get_grade() == 'Error'


class TestStudentModel():
    """"""
    pass


class TestClassroomModel:
    """"""

    def test_classroom_str(self):
        """"""

        classroom = mixer.blend(Classroom, name='test classroom')
        assert str(classroom) == 'test classroom'
