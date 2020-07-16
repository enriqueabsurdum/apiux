"""API views."""

# Django REST framework
from rest_framework import viewsets

# Models
from .models import Author, Book

# Serializers
from .serializers import AuthorSerializer, BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """Book Views class."""

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """Author Views class."""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
