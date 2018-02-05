from django.db import models
from evaluaciones.models import Universidad


class Universidad(models.Model):
    nombre_universidad = models.CharField(max_length=80, blank=False)
    acronimo_universidad = models.CharField(max_length=10, blank=False, unique=True)
    contacto = models.PositiveIntegerField(verbose_name='Contacto', unique=True)
    pagina_web = models.URLField(verbose_name='Página Web', unique=True)

    def __str__(self):
        return self.nombre_universidad


    class Meta:
        verbose_name = 'Universidad'
        verbose_name_plural = 'Universidades'
        ordering = ['id']


class Facultad(models.Model):
    nombre_facultad = models.CharField(max_length=80, blank=False)
    universidad = models.ForeignKey('Universidad', on_delete=models.CASCADE,)
    pagina_web = models.URLField(verbose_name='Página Web', unique=True)
    contacto = models.PositiveIntegerField(verbose_name='Contacto', unique=True)

    def __str__(self):
        return self.nombre_facultad

    class Meta:
        verbose_name = 'Facultad'
        verbose_name_plural = 'Facultades'
        ordering = ['nombre_facultad']

class Carrera(models.Model):
    nombre_carrera = models.CharField(max_length=80, blank=False)
    universidad = models.ForeignKey('Universidad', on_delete=models.CASCADE)
    facultad = models.ForeignKey('Facultad', on_delete=models.CASCADE)
    cantidad_materias = models.PositiveIntegerField(verbose_name='Cantidad de materias')

    def __str__(self):
        return self.nombre_carrera

    class Meta:
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'
        ordering = ['universidad']
