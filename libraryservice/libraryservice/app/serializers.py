from rest_framework import serializers
from .models import Books, BooksBorrow


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class BookBorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksBorrow
        fields = '__all__'
        read_only_fields = ('active',)
