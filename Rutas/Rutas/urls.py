"""
URL configuration for Rutas project.
"""
from django.contrib import admin
from django.urls import path

# Importaciones de tus vistas y módulos de la app
from . import vistas
from . import view
from Rutas import apirest  # Corregido: sintaxis correcta para importar el módulo

# Importaciones de drf-yasg
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración del esquema de Swagger
schema_view = get_schema_view(
    openapi.Info(  # Corregido: 'Info' con mayúscula
        title="API de Rutas",
        default_version='v1',  # Añadido: es obligatorio para drf-yasg
        description="Documentación de la API de Rutas",
    ),
    public=True,  # Corregido: 'True' con mayúscula
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenido/', vistas.bienvenido, name='bienvenido'),
    path('bienvenido2/', view.bienvenido, name='bienvenido2'),
    path('api/mensaje/', apirest.mensaje, name='api-mensaje'),
    path('api/guardar/', apirest.guardar, name='api-guardar'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]