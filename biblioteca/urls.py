# biblioteca/urls.py
from django.urls import path
from .views import LibroListView

urlpatterns = [
    path('listado/', LibroListView.as_view(), name='listado_libros'),
]