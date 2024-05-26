from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from core.models import(
    Course,
    Lecture,
    Student
)

from attendance import (
    serializers,
)

# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CourseSerializer
    queryset = Course.objects.all()

class StudentImageViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StudentImageSerializer
    queryset = Student.objects.all()

class LectureViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LectureSerializer
    queryset = Lecture.objects.all()

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.StudentSerializer
    queryset = Student.objects.all()