from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from core import models

from attendance.serializers import StudentSerializer

import tempfile
import os
from PIL import Image

def image_upload_url():
    return reverse('attendance:studentimage-list')

class StudentAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_student(self):
        """Test creating a new student"""
        payload = {
            'first_name': 'John',
            'last_name': 'Doe',
            'age': 25,
            'email': 'john@mail.com',
        }

        res = self.client.post(reverse('attendance:student-list'), payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        student = models.Student.objects.get(id=res.data['id'])
        for k, v in payload.items():
            self.assertEqual(getattr(student, k), v)

    def test_retrieve_students(self):
        """Test retrieving a list of students"""
        models.Student.objects.create(
            first_name = 'John',
            last_name = 'Doe',
            age = 25,
            email = 'jhon@mail.com',
        )
        models.Student.objects.create(
            first_name = 'Jane',
            last_name = 'Doe',
            age = 22,
            email = 'jane@mail.com',
        )

        res = self.client.get(reverse('attendance:student-list'))

        students = models.Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)


class ImageUploadTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.student = models.Student.objects.create(
            first_name = 'John',
            last_name = 'Doe',
            age = 25,
            email = 'john@mail.com',
        )

    def tearDown(self):
        image = models.StudentImage.objects.all().delete()

    def test_upload_image(self):
        """Test uploading an image to student"""
        url = image_upload_url()
        with tempfile.NamedTemporaryFile(suffix='.jpg') as image_file:
            img = Image.new('RGB', (10, 10))
            img.save(image_file, format='JPEG')
            image_file.seek(0)
            payload = {
                'student': self.student.id,
                'image': image_file,
            }
            res = self.client.post(url, payload, format='multipart')

        student_image = models.StudentImage.objects.get(student=self.student)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIn('image', res.data)
        self.assertTrue(os.path.exists(student_image.image.path))

    def test_upload_image_bad_request(self):
        """Test uploading an invalid image"""
        url = image_upload_url()
        payload = {
            'student': self.student.id,
            'image': 'notimage',
        }
        res = self.client.post(url, payload, format='multipart')

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)