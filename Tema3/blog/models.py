from django.conf import settings

from django.db import models

from django.utils import timezone

# Create your models here.


class Usuario(models.Model):

    nombre = models.CharField(max_length=200)
    correoElectronico = models.CharField(max_length=200,unique=True)
    contrasena = models.CharField(max_length=200)
    fechaRegistro = models.DateField()
    
    

    def __str__(self):
        return ("Nombre: " + self.nombre +
                "Correo Electronico: " + self.correoElectronico +
                "Contraseña: " + self.contrasena + 
                "Fecha de registro:" + self.fechaRegistro)

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    estado=[
        ("Pendiente", "Pendiente"),
        ("Progreso", "Progreso"),
        ("Completada", "Completada"),
    ]
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateField()
    hora_vencimiento = models.TimeField()
    
    def __str__(self):
        return (
            "Título: " + self.titulo +
            " Descripción: " + self.descripcion +
            " Prioridad: " + str(self.prioridad) +
            " Estado: " + self.estado +
            " Completada: " + str(self.completada) +
            " Fecha de creación: " + str(self.fecha_creacion) +
            " Hora de vencimiento: " + str(self.hora_vencimiento)
        )
    
class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    usuarios = models.ManyToManyField(Usuario, through='AsignaProyectos', related_name="proyectos")
    proyectos = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __str__(self):
         return (
            "Nombre: " + self.nombre +
            "Descripción: " + self.descripcion +
            "Duración estimada: " + self.duracion_estimada + 
            "Fecha de inicio: " + self.fecha_inicio +
            "Fecha de finalización: " + self.fecha_finalizacion
        )

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class AsignacionTarea(models.Model):
    observaciones = models.TextField(blank=True)
    fecha_asignacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return ("Observaciones: " + self.observaciones + 
                "Fecha de asignacion: " + self.fecha_asignacion)


class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return ("Comentario de " + self.usuario + "en " + self.tarea)
    
    
    
class AsignaProyectos(models.Model):
    usuarios = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    proyectos = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    
    def __str__(self):
            return ("Usuario: " + self.usuarios + 
                    "Proyectos: " + self.proyectos)