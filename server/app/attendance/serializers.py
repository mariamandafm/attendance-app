from rest_framework import serializers

from core.models import(
    Course,
    Lecture,
    Student,
    StudentImage,
)

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description']
        read_only_fields = ['id']


class StudentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentImage
        fields = ['id', 'student', 'image']
        read_only_fields = ['id']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'age', 'email', 'courses']
        read_only_fields = ['id']

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id', 'date', 'content', 'course']
        read_only_fields = ['id']