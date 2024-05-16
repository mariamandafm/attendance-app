from rest_framework import viewsets

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