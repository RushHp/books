from django.db import models

"""Книги"""


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    author = models.CharField(max_length=255, default='', verbose_name="Автор")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT, null=True, verbose_name="Жанр")

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['name', 'author', 'genre', 'price']

    def __str__(self):
        return self.name


"""Жанры"""


class Genre(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='Жанр')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']

    def __str__(self):
        return self.name
