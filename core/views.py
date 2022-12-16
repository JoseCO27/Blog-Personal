from django.shortcuts import render, HttpResponse
# Create your views here.
def index(request):
    # Recibe el request y responde con el nombre de una plantilla
    return render(request, 'home.html')