from django.db import models


class Student(models.Model):
    """Class for Student object."""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_number = models.IntegerField(unique=True)
    is_qualified = models.BooleanField(default=False)
    average_score = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_grade(self):
        if self.average_score < 40:
            return 'Fail'
        elif self.average_score < 70 > 40:
            return 'Pass'
        elif self.average_score < 100 > 70:
            return 'Excellent'
        else:
            return 'Error'


class Classroom(models.Model):
    """Class for Classroom object."""

    name = models.CharField(max_length=120)
    student_capacity = models.IntegerField()
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
