from django.contrib import admin

# Register your models here.
from core import models

admin.site.register(models.Course)
admin.site.register(models.Lecture)
admin.site.register(models.Student)