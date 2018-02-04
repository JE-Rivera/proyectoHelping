from django.db import models

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