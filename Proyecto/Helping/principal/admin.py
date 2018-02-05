from django.contrib import admin
from . import models


class FacultadInline(admin.StackedInline):
    model = models.Facultad
    extra = 1


class CarreraInline(admin.StackedInline):
    model = models.Carrera
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
    inlines = [CarreraInline]


@admin.register(models.Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ['nombre_carrera', 'facultad', 'universidad', 'cantidad_materias']
    fieldsets = [
        ('Detalles', {'fields': ['nombre_carrera', 'cantidad_materias']}),
        ('Información de la Carrera', {'fields': ['universidad', 'facultad']}),
    ]

