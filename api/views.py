from rest_framework import generics
from classroom.models import Student, Classroom
from api.serializers import StudentSerializer


class StudentListApiView(generics.ListAPIView):
    """ListApiView for Student model."""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailsApiView(generics.RetrieveAPIView):
    """DetailsApiView for Student object."""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCreateApiView(generics.CreateAPIView):
    """CreateApiView for Student object."""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDeleteApiView(generics.DestroyAPIView):
    """DeleteApiView for Student object."""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
