from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer, Books, BooksBorrow, BookBorrowSerializer
from rest_framework import filters
from rest_framework import generics
from rest_framework.exceptions import ValidationError, ParseError


# Create your views here.

class BooksViewSets(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Books.objects.all().order_by('-id')
    filter_backends = [filters.SearchFilter]
    search_fields = ['book_name', 'author']


class BooksBorrowViewSets(generics.ListCreateAPIView):
    serializer_class = BookBorrowSerializer

    # queryset = BooksBorrow.objects.all().order_by('-id')
    # search_fields = ['book__book_name', 'book__author']
    def get_queryset(self):
        if not 'student_id' in self.request.GET:
            raise ValidationError("Student id not provided")

        student_id = self.request.GET['student_id']
        queryset = BooksBorrow.objects.filter(student_id=student_id)
        return queryset
