from django.db import models
# Ckeditor
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    image = models.ImageField(verbose_name='Imagen', upload_to='blog/')
    title = models.CharField(max_length=200, verbose_name='Título')
    descripcion = models.TextField(verbose_name='Descripción')
    contenido = RichTextField(verbose_name='Contenido')
    
    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de Creación')
    fecha_act = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de actualización')
    
    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.title
