"""
URL configuration for AgendaDeLibros project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,  re_path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi\

from contactos.views import (
    lista_libros,
    lista_libros_paginados,
    ver_libro,
    crear_libro,
    actualizar_libro,
    eliminar_libro
)

schema_view = get_schema_view(
    openapi.Info(
        title="API Gestión de Libros",
        default_version='v1',
        description="CRUD de Gestión de Libros",
        terms_of_service="https://www.tus-terminos.com/",
        contact=openapi.Contact(email="contacto@tudominio.com"),
        license=openapi.License(name="Licencia XYZ"),
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('libros/', lista_libros, name='lista_libros'),
    path('libros/paginados/<int:page>/', lista_libros_paginados, name='lista_libros_paginados'),
    path('libros/view/<int:id>/', ver_libro, name='ver_libro'),
    path('libros/crear/', crear_libro, name='crear_libro'),
    path('libros/actualizar/', actualizar_libro, name='actualizar_libro'),
    path('libros/eliminar/<int:id>/', eliminar_libro, name='eliminar_libro'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]