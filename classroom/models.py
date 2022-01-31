from django.db import models


class Classroom(models.Model):
    """Class for Classroom object"""

    name = models.CharField(max_length=120)
    student_capacity = models.IntegerField()
    students = models.ManyToManyField('Test')

    def __str__(self):
        return self.name
