from django.shortcuts import render
from .models import Entrenador, Clase, Socio

# Create your views here.
def index (request):
    return render(request, 'gym/index.html')

def entrenador_list(request):
    entrenadores = Entrenador.objects.all()
    return render(request, 'gym/entrenador_list.html', {'entrenadores_mostrar': entrenadores})


def clase_list(request):
    clases = Clase.objects.all()
    return render(request, 'gym/clase_list.html', {'clases_mostrar': clases})


def socio_list(request):
    socios = Socio.objects.all()
    return render(request, 'gym/socio_list.html', {'socios_mostrar': socios})