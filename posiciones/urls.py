from django.urls import include, path
from . import views


urlpatterns = [
    path('cargar-equipo/', views.cargar_equipo, name='cargar_equipo'),
    path('cargar-resultados/', views.cargar_resultados, name='cargar_resultados'),
    path('tabla/', views.tabla, name='tabla'),
]