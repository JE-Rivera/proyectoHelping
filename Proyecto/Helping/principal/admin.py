from django.contrib import admin
from . import models


@admin.register(models.Universidad)
class UniversidadAdmin(admin.ModelAdmin):
    list_display = ['nombre_universidad', 'acronimo_universidad', 'contacto', 'pagina_web']
    fieldsets = [
        ('Detalles', {'fields': ['nombre_universidad', 'acronimo_universidad']}),
        ('Información de contacto', {'fields': ['contacto', 'pagina_web']}),
    ]


