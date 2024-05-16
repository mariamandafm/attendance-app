from rest_framework.routers import DefaultRouter
from attendance import views
from django.urls import path, include

router = DefaultRouter()
router.register('courses', views.CourseViewSet)

app_name = 'attendance'

urlpatterns = [
    path('', include(router.urls))
]