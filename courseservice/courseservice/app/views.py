from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CourseSerializer, Course, CourseEnrollmentSerializer, CourseEnrollment
from rest_framework import filters
from rest_framework import generics
from rest_framework.exceptions import ValidationError, ParseError


# Create your views here.

class CourseViewSets(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all().order_by('-id')
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'code']


class CourseEnrollViewSets(generics.ListCreateAPIView):
    serializer_class = CourseEnrollmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['course__title', 'course__code']

    def get_queryset(self):
        if not 'student_id' in self.request.GET:
            raise ValidationError("Student id not provided")

        student_id = self.request.GET['student_id']
        queryset = CourseEnrollment.objects.filter(student_id=student_id)
        return queryset
