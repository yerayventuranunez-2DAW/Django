from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    correoElectronico = models.CharField(max_length=200, unique=True)
    contrasena = models.CharField(max_length=200)
    fechaRegistro = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return ("Nombre: " + self.nombre +
                " Correo Electronico: " + self.correoElectronico)


class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    duracion_estimada = models.FloatField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    usuarios = models.ManyToManyField(
        Usuario, through="AsignaProyectos", related_name="proyectos"
    )
    creador = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name="proyectos_creados"
    )

    def __str__(self):
        return ("Nombre: " + self.nombre +
                " Descripción: " + self.descripcion +
                " Duración estimada: " + str(self.duracion_estimada) +
                " Fecha de inicio: " + str(self.fecha_inicio) +
                " Fecha de finalización: " + str(self.fecha_finalizacion))


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    ESTADOS = [
        ("Pendiente", "Pendiente"),
        ("Progreso", "Progreso"),
        ("Completada", "Completada"),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default="Pendiente")
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateField()
    hora_vencimiento = models.TimeField()
    creador = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name="tareas_creadas"
    )
    proyecto = models.ForeignKey(
        Proyecto, on_delete=models.CASCADE, related_name="tareas"
    )
    etiquetas = models.ManyToManyField(Etiqueta, related_name="tareas", blank=True)
    usuarios = models.ManyToManyField(
        Usuario, through="AsignacionTarea", related_name="tareas_asignadas"
    )

    def __str__(self):
        return ("Título: " + self.titulo +
                " Descripción: " + self.descripcion +
                " Prioridad: " + str(self.prioridad) +
                " Estado: " + self.estado +
                " Completada: " + str(self.completada) +
                " Fecha de creación: " + str(self.fecha_creacion) +
                " Hora de vencimiento: " + str(self.hora_vencimiento))


class AsignacionTarea(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True)
    fecha_asignacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return ("Observaciones: " + self.observaciones +
                " Fecha de asignacion: " + str(self.fecha_asignacion) +
                " Usuario asignado: " + self.usuario.nombre)


class Comentario(models.Model):
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name="comentarios"
    )
    tarea = models.ForeignKey(
        Tarea, on_delete=models.CASCADE, related_name="comentarios"
    )

    def __str__(self):
        return "Comentario de " + self.autor.nombre + " en " + self.tarea.titulo


class AsignaProyectos(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return ("Usuario: " + self.usuario.nombre +
                " Proyecto: " + self.proyecto.nombre)