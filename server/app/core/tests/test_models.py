from django.test import TestCase
from core import models

class ModelTests(TestCase):
    def test_create_course(self):
        """Test creating a new course is successful"""
        course = models.Course.objects.create(
            title = 'Python',
            description = 'Python programming language'
        )

        self.assertEqual(str(course), course.title)

    def test_create_lecture(self):
        """Test creating a new lecture is successful"""
        course = models.Course.objects.create(
            title = 'Python',
            description = 'Python programming language'
        )
        lecture = models.Lecture.objects.create(
            date = '2021-08-17',
            content = 'Python basics',
            course = course
        )

        self.assertEqual(str(lecture), f'{course.title} - {lecture.date}')

    def test_create_student(self):
        """Test creating a new student is successful"""
        course = models.Course.objects.create(
            title = 'Python',
            description = 'Python programming language'
        )
        student = models.Student.objects.create(
            first_name = 'John',
            last_name = 'Doe',
            age = 25,
            email = 'john@mail.com',
        )
        student.courses.add(course)

        self.assertEqual(str(student), f'{student.first_name} {student.last_name}')



