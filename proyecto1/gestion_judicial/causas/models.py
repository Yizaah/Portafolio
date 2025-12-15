from django.db import models
from clientes.models import Cliente

class Competencia(models.TextChoices):
    CORTE_SUPREMA = 'CS', 'Corte Suprema'
    CORTE_APELACIONES = 'CA', 'Corte de Apelaciones'
    CIVIL = 'C', 'Civil'
    FAMILIA = 'F', 'Familia'
    PENAL = 'P', 'Penal'
    LABORAL = 'L', 'Laboral'
    COBRANZA = 'CO', 'Cobranza'


class EstadoCausa(models.TextChoices):
    ACTIVA = 'ACT', 'Activa'
    ARCHIVADA = 'ARC', 'Archivada'
    NO_ACTIVA = 'NOA', 'No activa'

class Causa(models.Model):
    competencia = models.CharField(
        max_length=2,
        choices=Competencia.choices
    )

    corte = models.CharField(
        max_length=100,
        blank=True,
        help_text="Solo para causas que no sean de Corte Suprema"
    )

    tribunal = models.CharField(max_length=150)

    tipo_causa = models.CharField(
        max_length=5,
        help_text="Letra del rol de la causa (Ej: C, R, T, etc.)"
    )

    rol = models.PositiveIntegerField()
    anio = models.PositiveIntegerField()

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name='causas'
    )

    descripcion = models.TextField(blank=True)

    estado = models.CharField(
        max_length=3,
        choices=EstadoCausa.choices,
        default=EstadoCausa.ACTIVA
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('tipo_causa', 'rol', 'anio', 'tribunal')
        ordering = ['-anio', 'tipo_causa', 'rol']

    def __str__(self):
        return f"{self.tipo_causa}-{self.rol}-{self.anio}"
