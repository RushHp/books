from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from store.views import BookViewSet

# Пробрасываем запрос из приложения к view который обратится к модели и ее сериализует.
router = SimpleRouter()
# Добавить в роутер view c урлом book и указываю view.
router.register(r'book', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Добавляю урлы роутера.
urlpatterns += router.urls
