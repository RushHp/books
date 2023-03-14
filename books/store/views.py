from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from store.models import Book
from store.serializers import BookSerializer


# Установка view для Book. Api endpoint.
class BookViewSet(ModelViewSet):
    # Запрос объекта из БД.
    queryset = Book.objects.all()
    # Класс сериализатор.
    serializer_class = BookSerializer

    # Фильтрация, поиск через API.
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    # По каким полям фильтровать.
    filterset_fields = ['price']
    # Поля по которым будем искать.
    search_fields = ['name', 'author']
    # Вывод по алфавиту или сортировка по цене.
    ordering_fields = ['price', 'author']
