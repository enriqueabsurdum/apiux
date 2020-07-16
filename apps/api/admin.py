"""API admin."""

# Django
from django.contrib import admin

# Models
from .models import Author, Book

admin.site.register(Author)
admin.site.register(Book)
