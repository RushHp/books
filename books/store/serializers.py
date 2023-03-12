from rest_framework.serializers import ModelSerializer

from store.models import Book


# Сериализатор rest. Используется во view.
class BookSerializer(ModelSerializer):
    # Вложенный класс.
    class Meta:
        # Модель класса Book.
        model = Book
        # Все поля из модели.
        fields = '__all__'
