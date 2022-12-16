from django.contrib import admin

# Register your models here.
from .models import Post

#admin.site.register(Post)

# Clase para modificar o editar el panel Admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'descripcion', 'fecha_creacion')
    # Ponemos link en el campo TITLE
    list_display_links = ('id','title',)
    # Filtro por fecha de creacion y actualizacion
    list_filter = ('fecha_creacion', 'fecha_act',)
    # Buscador
    search_fields = ('title', 'descripcion',)

    # Campos en solo modo lectura
    readonly_fields = ('fecha_creacion', 'fecha_act') 

    

