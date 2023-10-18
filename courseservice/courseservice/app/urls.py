from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from .views import CourseViewSets, CourseEnrollViewSets

router = DefaultRouter()

router.register('course', CourseViewSets, basename="Course")

urlpatterns = [
    path('', include(router.urls)),
    path('course-enroll/', CourseEnrollViewSets.as_view(), name="Course Enroll"),
]
