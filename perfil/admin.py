from django.contrib import admin

# models
from .models import Project

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
# Mostrar los campos 
    list_display = ('id', 'title', 'descripcion', 'fecha_creacion',)
    list_editable = ('title', 'descripcion',)
    list_filter = ('title', 'fecha_creacion', 'fecha_act',)
    search_fields = ('title',)

#admin.site.register(Project)