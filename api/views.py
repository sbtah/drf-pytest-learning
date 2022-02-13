from rest_framework import generics, status
from rest_framework.views import APIView, Response
from classroom.models import Student, Classroom
from api.serializers import StudentSerializer, ClassroomSerializer


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


# Classroom Views - made with APIView just for practice.
class ClassroomListApiView(APIView):
    """ListApiView for Classrooms of specified capacity for Students."""

    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

    def get(self, request, *args, **kwargs):
        """GET method."""
        items = Classroom.objects.all()
        serializer = ClassroomSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClassroomStudentCapacityApiView(APIView):
    """Return classrooms with student capacity greater or equal to link param."""

    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

    def get(self, request, *args, **kwargs):
        """Custom GET method."""
        url_number = self.kwargs.get('student_capacity')
        items = Classroom.objects.filter(student_capacity__gte=url_number)
        serializer = ClassroomSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
