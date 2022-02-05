from rest_framework import serializers
from classroom.models import Student, Classroom


class StudentSerializer(serializers.ModelSerializer):
    """Serializer for Student Object."""

    class Meta:
        model = Student
        fields = ('first_name',
                  'last_name',
                  'user_number',
                  'slug',
                  'is_qualified',
                  'average_score'
                  )
