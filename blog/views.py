from django.shortcuts import render, HttpResponse
# models
from .models import Post

# Create your views here.
def posts(request):
    return HttpResponse('<h1>Página de Publicaciones </h1>')
    

# Recuperar los blocs y el id
def posts(request):
    # Obtenemos el primer registro
    first_post = Post.objects.first()
    posts = Post.objects.all()
    #return HttpResponse(blogs)
    return render(request, 'blogs.html', {'posts':posts, 'first_post': first_post})
    
def post(request, id):
    post = Post.objects.get(id=id)
    # enviamos al html por id
    # contenido = f'{blog.title} - {blog.descripcion}'
    # return render(request, 'blog.html')
    return render(request, 'blog.html', {'post':post})

