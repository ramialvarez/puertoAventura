from django.shortcuts import render, redirect
from .forms import FormularioRegistrarPublicacion
from django.contrib import messages
from db.models import Post,User
from autenticacion.views import se_encuentra_conectado

# Create your views here.

def registrar_publicacion(request):

    errorPatente = None
    if request.method == 'POST':
        form = FormularioRegistrarPublicacion(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = User.objects.get(email=se_encuentra_conectado(request)[0]) # Assign the current user to the post
            post.save()
            messages.success(request, "Publicacion registrada exitosamente")
            return redirect("/")
        else:
            errorPatente = form.errors['patent']
            messages.error(request, "Ya existe una publicacion registrada en el sistema con esa patente")
    else:
        form = FormularioRegistrarPublicacion()
        print(form.errors)
    print(errorPatente)
    return render(request, 'registrar_publicacion.html', {'form': form, 'usuario': se_encuentra_conectado(request), 'patente': errorPatente})

def ver_publicaciones(request):
    posts = Post.objects.all()
    for post in posts:
        user = User.objects.get(email=post.user_id)
    return render(request, "ver_publicaciones.html", {"posts": posts,'usuario': se_encuentra_conectado(request)})


def ver_publicacion(request, post_id):
    
    post = Post.objects.get(id=post_id)
    user = User.objects.get(email=post.user_id)
    return render(request, "ver_publicacion.html", {"post": post,'usuario': se_encuentra_conectado(request)})

def ver_imagen(request, post_id):
    
    post = Post.objects.get(id=post_id)
    return render(request, "ver_publicacion.html", {"image": post.image,'usuario': se_encuentra_conectado(request)})
