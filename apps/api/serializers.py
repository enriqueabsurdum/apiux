"""API serializers."""

# Django REST framework
from rest_framework import serializers

# Models
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """Model class serializer Book."""

    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    """Model class serializer Author."""

    books = BookSerializer(many=True, required=False)

    class Meta:
        model = Author
        fields = (
            'id', 'name', 'nationality', 'created', 'updated', 'books'
        )
