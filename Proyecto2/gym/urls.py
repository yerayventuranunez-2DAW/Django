from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index.html'),
    path('entrenador/', views.entrenador_list, name='entrenador_list'),
    path('clases/', views.clase_list, name='clase_list'),
    path('socios/', views.socio_list, name='socio_list'),
]