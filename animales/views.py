from django.shortcuts import render
from .models import Animal, Protectora, Colaborador
# Create your views here.

def animal_list(request):
    animales = Animal.objects.all()
    return render(request, 'animales/animal_list.html', {'animales_mostrar': animales})


def protectora_list(request):
    protectoras = Protectora.objects.all()
    return render(request, 'animales/protectora_list.html', {'protectoras_mostrar': protectoras})


def colaborador_list(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'animales/colaborador_list.html', {'colaboradores_mostrar': colaboradores})