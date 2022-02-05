from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


def average_grade_validator(val):
    """Custom validator for average score."""

    if val < 0:
        raise ValidationError(
            _(f'{val} is less then 0'),
            params={'value': val}
        )


def name_validator(val):
    """Custom validator for first_name and last_name"""

    if len(val) < 2:
        raise ValidationError(
            _('Should be letters only and more then 1 character long'),
            params={'value': val}
        )

    elif not val.isalpha():
        raise ValidationError(
            _('Should be letters only and more then 1 character long'),
            params={'value': val}
        )


class Student(models.Model):
    """Class for Student object."""

    first_name = models.CharField(max_length=50, validators=[name_validator])
    last_name = models.CharField(max_length=50, validators=[name_validator])
    user_number = models.IntegerField(unique=True)
    slug = models.SlugField(blank=True, null=True)
    is_qualified = models.BooleanField(default=False)
    average_score = models.FloatField(
        blank=True,
        null=True,
        validators=[average_grade_validator]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_grade(self):
        if 0 <= self.average_score < 40:
            return 'Fail'
        elif self.average_score < 70 >= 40:
            return 'Pass'
        elif self.average_score <= 100 >= 70:
            return 'Excellent'
        else:
            return 'Error'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        super(Student, self).save(*args, **kwargs)


class Classroom(models.Model):
    """Class for Classroom object."""

    name = models.CharField(max_length=120)
    student_capacity = models.IntegerField()
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
