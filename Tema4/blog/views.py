from django.shortcuts import render
from .models import Proyecto, Tarea, AsignacionTarea, Comentario

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def listar_proyectos(request):
    proyectos = Proyecto.objects.select_related('creador').prefetch_related('usuarios').all()
    return render(request, 'proyectos.html', {'proyectos': proyectos})

def tareas_proyecto(request, proyecto_id):
    tareas = Tarea.objects.filter(proyecto_id=proyecto_id).order_by('-fecha_creacion')
    proyecto = Proyecto.objects.get(id=proyecto_id)
    
    return render(request, 'lista.html', {'tareas':tareas, 'proyecto': proyecto})

def usuario_tareas(request, tarea_id):
    usuario = AsignacionTarea.objects.filter(tarea_id=tarea_id).order_by('fecha_asignacion')
    tarea = Tarea.objects.get(id=tarea_id)
    
    return render(request,'listaUsuarioTarea.html', {'usuarios': usuario, 'tarea': tarea})

def tareas_observaciones(request, texto):
    tareas = Tarea.objects.filter(asignaciontarea__observaciones__icontains=texto).distinct()
    
    return render(request, 'tareas_observaciones.html',{'tareas': tareas, 'texto_buscado': texto})

def tareas_completadas(request,anyo_inicio,anyo_fin):
    tareas = Tarea.objects.filter(fecha_creacion__year__gte=anyo_inicio,fecha_creacion__year__lte=anyo_fin,estado='Completada')
    
    return render(request, 'tareas_completada.html', {'tareas': tareas,'anyo_inicio':anyo_inicio,'anyo_fin': anyo_fin})

def ultimo_comentario_proyecto(request, proyecto_id):
    ultimo_comentario = Comentario.objects.filter(tarea__proyecto_id=proyecto_id).order_by('-fecha_comentario')[:1].get()
    
    return render(request, 'ultimo_comentario.html', {'comentario': ultimo_comentario})

def comentarios_filtrados(request, tarea_id, palabra, anyo):
    comentarios = Comentario.objects.filter(tarea_id=tarea_id,contenido__startswith=palabra,fecha_comentario__year = anyo).order_by('fecha_comentario')
    tarea = Tarea.objects.get(id=tarea_id)
    
    return render(request, 'comentarios_filtrados.html', {'comentarios': comentarios,'tarea': tarea,'palabra': palabra,'anyo': anyo}) 