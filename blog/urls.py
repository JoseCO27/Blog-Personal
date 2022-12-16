from django.urls import path

#Vistas
from . import views

# Config URL
urlpatterns = [
    path('', views.posts, name='posts'),
    # Que envie el id del blog a publicar
    path('<int:id>', views.post, name='post'),
]