from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from core import models

from attendance.serializers import CourseSerializer

class CourseAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_course(self):
        """Test creating a new course"""
        payload = {
            'title': 'Python',
            'description': 'Python programming language'
        }
        res = self.client.post(reverse('attendance:course-list'), payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        course = models.Course.objects.get(id=res.data['id'])
        for k, v in payload.items():
            self.assertEqual(getattr(course, k), v)

    def test_retrieve_courses(self):
        """Test retrieving a list of courses"""
        models.Course.objects.create(
            title = 'Python',
            description = 'Python programming language'
        )
        models.Course.objects.create(
            title = 'JavaScript',
            description = 'JavaScript programming language'
        )

        res = self.client.get(reverse('attendance:course-list'))

        courses = models.Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)