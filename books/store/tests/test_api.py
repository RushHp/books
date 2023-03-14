from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from store.models import Book
from store.serializers import BookSerializer


class BooksApiTestCase(APITestCase):
    def setUp(self):
        # Показать книги.
        self.book_1 = Book.objects.create(name='Test book 1', price=258, author='Author 1')
        self.book_2 = Book.objects.create(name='Test book 2', price=344, author='Author 5')
        self.book_3 = Book.objects.create(name='Test book Author 1', price=544, author='Author 3')

    def test_get(self):
        # Получение списка книг.
        url = reverse('book-list')
        print(f'Показать URL: {url}')
        # Клиент, который делает запрос к серверу.
        response = self.client.get(url)
        print(f'Показать ответ: {response.data}')
        # Проверка полей (не поменялось ли там что-то без нашего ведома).
        serializer_data = BookSerializer([self.book_1, self.book_2, self.book_3], many=True).data
        self.assertEqual(serializer_data, response.data)
        # Проверка статуса кода.
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_filter(self):
        # Получение списка книг.
        url = reverse('book-list')
        print(f'Показать URL: {url}')
        # Клиент, который делает запрос к серверу.
        response = self.client.get(url, data={'price': 258})
        print(f'Показать ответ: {response.data}')
        # Проверка полей (не поменялось ли там что-то без нашего ведома).
        serializer_data = BookSerializer([self.book_1, self.book_2, self.book_3], many=True).data
        self.assertEqual(serializer_data, response.data)
        # Проверка статуса кода.
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_search(self):
        # Получение списка книг.
        url = reverse('book-list')
        print(f'Показать URL: {url}')
        # Ищем по Author 1.
        response = self.client.get(url, data={'search': 'Author 1'})
        print(f'Показать ответ: {response.data}')
        # Проверка полей (не поменялось ли там что-то без нашего ведома).
        serializer_data = BookSerializer([self.book_1, self.book_3], many=True).data
        self.assertEqual(serializer_data, response.data)
        # Проверка статуса кода.
        self.assertEqual(status.HTTP_200_OK, response.status_code)
