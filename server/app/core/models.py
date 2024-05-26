from django.db import models

import uuid
import os

def student_image_file_path(instance, filename):
    """Generate file path for new student image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/student/', filename)

class Lecture(models.Model):
    date = models.DateField()
    content = models.TextField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course.title} - {self.date}'

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class StudentImage(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=student_image_file_path)

    def __str__(self):
        return f"{self.student.first_name} image {self.id}"