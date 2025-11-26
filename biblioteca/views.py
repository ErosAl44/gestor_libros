# biblioteca/views.py

from django.views.generic import ListView
from .models import Libro

class LibroListView(ListView):
    model = Libro
    template_name = 'biblioteca/libro_listado.html'
    context_object_name = 'libros'

# Asegúrate de que no haya ninguna línea extra, especialmente:
# return self.titulo
# Y verifica que la indentación de la clase sea correcta (4 espacios por nivel).