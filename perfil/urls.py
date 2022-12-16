from django.urls import path

#Vistas
from . import views

# Config URL
urlpatterns = [
    path('', views.perfil, name='profile'),
]