from rest_framework import serializers

from core.models import(
    Course,
    Lecture,
    Student
)

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description']
        read_only_fields = ['id']