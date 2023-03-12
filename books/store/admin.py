from django.contrib import admin
from .models import Book

# Регистрация модели в админке.
admin.site.register(Book)
