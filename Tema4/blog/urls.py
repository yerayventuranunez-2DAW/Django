from django.urls import path
from . import views


urlpatterns = [
    # Ejercicio 1
    path('', views.inicio, name='inicio'),
    # Ejercicio 2
    path('proyectos/', views.listar_proyectos, name='lista_proyectos'),
    # Ejercicio 3
    path('proyecto/<int:proyecto_id>/tareas/', views.tareas_proyecto, name='tareas_proyecto'),
    # Ejercicio 4
    path('tareas/<int:tarea_id>/usuario/', views.usuario_tareas, name='usuarios_tarea'),
    # Ejercicio 5
    path('tareas/observaciones/<str:texto>/', views.tareas_observaciones, name='tareas_observaciones'),
    # Ejericcio 6
    path('tareas/completadas/<int:anyo_inicio>/<int:anyo_fin>/', views.tareas_completadas, name='tareas_completadas'),
    # Ejercicio 7
    path('proyecto/<int:proyecto_id>/ultimo-comentario/', views.ultimo_comentario_proyecto, name='ultimo_comentario'),
    # Ejercicio 8
    path('tarea/<int:tarea_id>/comentarios/<str:palabra>/<int:anyo>/', views.comentarios_filtrados, name='comentarios_filtrados'),
]
