"""Utils models."""

# Django
from django.db import models


class BaseModel(models.Model):
    """
    Base model class:
    Utility based on a Django model, which integrates two attributes:
         - created: creation date.
         - updated: modification date.
    """

    created = models.DateTimeField(verbose_name='fecha creación', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='fecha modificación', auto_now=True)

    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-updated']
