from unittest import TestCase

from store.models import Book
from store.serializers import BookSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        """Сравниваем данные"""
        book_1 = Book.objects.create(name='Test book 1', price=258)
        book_2 = Book.objects.create(name='Test book 2', price=344)

        data = BookSerializer([book_1, book_2], many=True).data
        # Данные которые ожидаем.
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test book 1',
                'price': '258.00'
            },

            {
                'id': book_2.id,
                'name': 'Test book 2',
                'price': '344.00'
            },
        ]
        # Ожидаемые данные сравниваем с имеющимися из сериализатора.
        self.assertEqual(expected_data, data)
