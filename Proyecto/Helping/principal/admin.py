from django.contrib import admin
from . import models


class FacultadInline(admin.StackedInline):
    model = models.Facultad
    extra = 1


@admin.register(models.Universidad)
class UniversidadAdmin(admin.ModelAdmin):
    list_display = ['nombre_universidad', 'acronimo_universidad', 'contacto', 'pagina_web']
    fieldsets = [
        ('Detalles', {'fields': ['nombre_universidad', 'acronimo_universidad']}),
        ('Información de contacto', {'fields': ['contacto', 'pagina_web']}),
    ]
    inlines = [FacultadInline]


@admin.register(models.Facultad)
class FacultadAdmin(admin.ModelAdmin):
    list_display = ['nombre_facultad', 'universidad', 'pagina_web']
    fieldsets = [
        ('Detalles', {'fields': ['nombre_facultad', 'universidad']}),
        ('Información de contacto', {'fields': ['contacto', 'pagina_web']}),
    ]


