"""API URLs."""

# Django
from django.urls import include, path

# Django REST framework
from rest_framework.routers import DefaultRouter

# Views
from .views import AuthorViewSet, BookViewSet

router = DefaultRouter()
router.register('autor', AuthorViewSet)
router.register('libro', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
