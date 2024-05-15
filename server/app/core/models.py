from django.db import models

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
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'