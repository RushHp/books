from rest_framework.viewsets import ModelViewSet

from store.models import Book
from store.serializers import BookSerializer


# Установка view для Book. Api endpoint.
class BookViewSet(ModelViewSet):
    # Запрос объекта из БД.
    queryset = Book.objects.all()
    # Класс сериализатор.
    serializer_class = BookSerializer

