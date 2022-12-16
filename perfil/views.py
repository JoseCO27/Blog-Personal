from django.shortcuts import render, HttpResponse

# Models
from .models import Project

# Create your views here.
def perfil(request):
    """
    p1 = Project(title = "Información sobre HTML", descripcion="Descripción de HTML")
    p1.save()
    p2 = Project(title = "Curso de CSS", descripcion="Descripción de CSS")
    p2.save()    
    p3 = Project(title = "Curso de Django", descripcion="Descripción de Django")
    p3.save()
    """
    # Recupera los datos de la BD
    projects = Project.objects.all()
    #print(projects)
    #return HttpResponse('<h1>Página de Perfil</h1> {projects}')
    # Lo envia a la parte del cliente
    #return HttpResponse(projects)
    # return render(request, 'profile.html')
    return render(request, 'profile.html', {'projects':projects})