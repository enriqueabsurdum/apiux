"""API models."""

# Django
from django.db import models

# Utils
from apps.utils.models import BaseModel


class Author(BaseModel):
    """Model class Author."""

    name = models.CharField(
        unique=True,
        verbose_name='nombre',
        max_length=128
    )
    nationality = models.CharField(
        verbose_name='nacionalidad',
        max_length=64
    )

    class Meta:
        verbose_name = 'autor'
        verbose_name_plural = 'autores'

    def __str__(self):
        """Returns the name of the created Author."""
        return self.name


class Book(BaseModel):
    """Model class Book."""

    title = models.CharField(
        unique=True,
        verbose_name='título',
        max_length=256
    )
    author = models.ForeignKey(
        'Author',
        verbose_name='autor',
        related_name='books',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'libro'
        verbose_name_plural = 'libros'

    def __str__(self):
        """Returns the title of the created Book."""
        return self.title
