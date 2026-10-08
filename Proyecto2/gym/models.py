from django.db import models
from django.utils import timezone

# Create your models here.

class Entrenador(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    fecha_contratacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre


class Clase(models.Model):
    entrenador = models.ForeignKey(Entrenador, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    cuota_mensual = models.DecimalField(max_digits=6, decimal_places=2)
    fecha_alta = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre