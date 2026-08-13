from django.urls import path
from . import views

urlpatterns = [
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/paginados/<int:page>/', views.lista_libros_paginados, name='lista_libros_paginados'),
    path('libros/view/<int:id>/', views.ver_libro, name='ver_libro'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
    path('libros/actualizar/', views.actualizar_libro, name='actualizar_libro'),
    path('libros/eliminar/<int:id>/', views.eliminar_libro, name='eliminar_libro'),
]
