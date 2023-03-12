from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from store.models import Book
from store.serializers import BookSerializer


class BooksApiTestCase(APITestCase):
    def test_get(self):
        # Показать книги.
        book_1 = Book.objects.create(name='Test book 1', price=258)
        book_2 = Book.objects.create(name='Test book 2', price=344)
        # Получение списка книг.
        url = reverse('book-list')
        print(f'Показать URL: {url}')
        # Клиент, который делает запрос к серверу.
        response = self.client.get(url)
        print(f'Показать ответ: {response.data}')
        # Проверка полей (не поменялось ли там что-то без нашего ведома).
        serializer_data = BookSerializer([book_1, book_2], many=True).data
        self.assertEqual(serializer_data, response.data)
        # Проверка статуса кода.
        self.assertEqual(status.HTTP_200_OK, response.status_code)
