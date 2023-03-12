from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название книги')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name