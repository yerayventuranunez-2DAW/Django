from django.shortcuts import render
from .models import Proyecto, Tarea, AsignacionTarea, Comentario, Usuario
from django.views.defaults import page_not_found
from django.core.exceptions import PermissionDenied, SuspiciousOperation
from django.http import Http404
# Create your views here.
    # Ejercicio 1
def inicio(request):
    return render(request, 'inicio.html')
    
    # Ejercicio 2
def listar_proyectos(request):
    proyectos = Proyecto.objects.select_related('creador').prefetch_related('usuarios').all()
    return render(request, 'proyectos.html', {'proyectos': proyectos})
    
    
    # Ejercicio 3
def tareas_proyecto(request, proyecto_id):
    tareas = Tarea.objects.select_related("proyecto").filter(proyecto_id=proyecto_id).order_by('-fecha_creacion')
    proyecto = Proyecto.objects.get(id=proyecto_id)
    
    return render(request, 'lista.html', {'tareas':tareas, 'proyecto': proyecto})
    
    # Ejercicio 4
def usuario_tareas(request, tarea_id):
    usuario = AsignacionTarea.objects.select_related("usuario","tarea").filter(tarea_id=tarea_id).order_by('fecha_asignacion')
    tarea = Tarea.objects.get(id=tarea_id)
    
    return render(request,'listaUsuarioTarea.html', {'usuarios': usuario, 'tarea': tarea})
    
    # Ejercicio 5
def tareas_observaciones(request, texto):
    tareas = Tarea.objects.filter(asignaciontarea__observaciones__icontains=texto).distinct()

    return render(request, 'tareas_observaciones.html',{'tareas': tareas, 'texto_buscado': texto})

    # Ejercicio 6
def tareas_completadas(request,anyo_inicio,anyo_fin):
    tareas = Tarea.objects.filter(fecha_creacion__year__gte=anyo_inicio,fecha_creacion__year__lte=anyo_fin,estado='Completada')
    
    return render(request, 'tareas_completada.html', {'tareas': tareas,'anyo_inicio':anyo_inicio,'anyo_fin': anyo_fin})

    # Ejercicio 7
def ultimo_comentario_proyecto(request, proyecto_id):
    ultimo_comentario = Comentario.objects.select_related("autor").filter(tarea__proyecto_id=proyecto_id).order_by('-fecha_comentario')[:1].get()
    
    return render(request, 'ultimo_comentario.html', {'comentario': ultimo_comentario})

    # Ejercicio 8
def comentarios_filtrados(request, tarea_id, palabra, anyo):
    comentarios = Comentario.objects.select_related("tarea").filter(tarea_id=tarea_id,contenido__startswith=palabra,fecha_comentario__year = anyo).order_by('fecha_comentario')
    tarea = Tarea.objects.get(id=tarea_id)
    
    return render(request, 'comentarios_filtrados.html', {'comentarios': comentarios,'tarea': tarea,'palabra': palabra,'anyo': anyo}) 

    #Ejercicio 9
def listar_etiquetas(request,id_proyecto):
    etiquetas = Tarea.objects.select_related("proyecto").prefetch_related("etiquetas").filter(proyecto_id=id_proyecto)
    proyecto = Proyecto.objects.get(id=id_proyecto)

    return render(request, 'listar_etiquetas.html' , {'etiquetas':etiquetas, 'proyecto':proyecto})

    #Ejercicio 10
def usuariosSinTarea(request):
    usuarios = Usuario.objects.filter(tareas_asignadas__isnull=True)
    
    return render(request, 'usuariosSinTarea.html', {'usuarios':usuarios})

    #Ejercicio 11
def mi_error_400(request,exception=None):
    return render(request, 'errores/400.html',None,None,400)

def mi_error_403(request,exception=None):
    return render(request, 'errores/403.html',None,None,403)

def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)

def mi_error_500(request):
    return render(request, 'errores/500.html',None,None,500)


# VISTAS TEMPORALES PARA PROBAR LOS ERRORES

def probar_400(request):
    raise SuspiciousOperation("Prueba intencional del error 400")

def probar_403(request):
    raise PermissionDenied("Prueba intencional del error 403")

def probar_404(request):
    raise Http404("Prueba intencional del error 404")

def probar_500(request):
    resultado = 1 / 0  # Esto fuerza un error 500 
    return render(request, 'inicio.html')