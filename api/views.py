from rest_framework import generics
from classroom.models import Student, Classroom
from api.serializers import StudentSerializer


class StudentListApiView(generics.ListAPIView):
    """ListApiView for Student model."""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
