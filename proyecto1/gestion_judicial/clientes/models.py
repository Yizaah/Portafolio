from django.db import models

class Cliente(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    direccion = models.CharField(max_length=255, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    descripcion = models.TextField(blank=True)

    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['apellidos', 'nombres']

    def __str__(self):
        return f"{self.apellidos}, {self.nombres} ({self.rut})"
