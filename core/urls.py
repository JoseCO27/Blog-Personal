from django.urls import path

#Vistas
from . import views

# Config URL
urlpatterns = [
    path('', views.index, name='home'),
]