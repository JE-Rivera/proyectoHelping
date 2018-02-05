from django.db import models
from principal.models import Facultad

class Materia(models.Model):
    codigo_materia = models.CharField(max_length=10, blank=False, unique=True)
    nombre_materia = models.CharField(max_length=80, blank=False)
    facultad = models.ForeignKey('Facultad', on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo_materia

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
        ordering = ['codigo_materia']
