# Generated by Django 4.0.1 on 2022-02-03 21:04

import classroom.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_student_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='average_score',
            field=models.FloatField(blank=True, null=True, validators=[classroom.models.average_grade_validator]),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=50, validators=[classroom.models.name_validator]),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=50, validators=[classroom.models.name_validator]),
        ),
    ]