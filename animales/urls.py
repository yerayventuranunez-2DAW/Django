from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_list, name='animal_list'),
    path('protectoras/', views.protectora_list, name='protectora_list'),
    path('colaboradores/', views.colaborador_list, name='colaborador_list'),
]