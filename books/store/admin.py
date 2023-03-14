from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Book, Genre


# Регистрация модели в админке.
@admin.register(Book)
class BookAdmin(ModelAdmin):
    list_display = ('id', 'name', 'author', 'genre', 'price')
    list_display_links = ('id', 'name', 'genre',)
    search_fields = ('name', 'genre', 'author')


@admin.register(Genre)
class GenreAdmin(ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
