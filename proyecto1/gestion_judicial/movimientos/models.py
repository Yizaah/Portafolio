from django.db import models
from causas.models import Causa

class Movimiento(models.Model):
    causa = models.ForeignKey(
        Causa,
        on_delete=models.CASCADE,
        related_name='movimientos'
    )

    fecha = models.DateField()
    descripcion = models.TextField()
    observaciones = models.TextField(blank=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha', '-fecha_creacion']

    def __str__(self):
        return f"Movimiento {self.fecha} - {self.causa}"

