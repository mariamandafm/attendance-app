from rest_framework.routers import DefaultRouter
from attendance import views
from django.urls import path, include

router = DefaultRouter()
router.register('courses', views.CourseViewSet)
router.register('student-images', views.StudentImageViewSet, basename='studentimage')
router.register('students', views.StudentViewSet)
router.register('lectures', views.LectureViewSet)

app_name = 'attendance'

urlpatterns = [
    path('', include(router.urls))
]