from django.contrib import admin
from django.urls import path, include
from book_store.views import LivroViewSet, AutorViewSet, ClienteViewSet, EditoraViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('livros', LivroViewSet, basename='Livro')
router.register('autores', AutorViewSet, basename='Autor')
router.register('clientes', ClienteViewSet, basename='Cliente')
router.register('editoras', EditoraViewSet, basename='Editora')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]