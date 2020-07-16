"""API admin."""

# Django
from django.contrib import admin

# Models
from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    """Author admin class."""

    search_fields = ('name', 'nationality')
    list_display = ('id', 'name', 'nationality')
    list_display_links = ('id', 'name')
    list_filter = ('created', 'updated')
    fieldsets = (
        ('Autor', {
            'fields': ('name', 'nationality'),
        }),
        ('Metadata', {
            'fields': ('created', 'updated'),
        })
    )
    readonly_fields = ('created', 'updated',)


class BookAdmin(admin.ModelAdmin):
    """Book admin class."""

    search_fields = ('title', 'author__name')
    list_display = ('id', 'title', 'author')
    list_display_links = ('id', 'title')
    list_filter = ('created', 'updated')
    fieldsets = (
        ('Libro', {
            'fields': ('title', 'author'),
        }),
        ('Metadata', {
            'fields': ('created', 'updated'),
        })
    )
    readonly_fields = ('created', 'updated',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
