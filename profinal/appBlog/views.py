from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from appBlog.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here. objetos. def, request
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
def index(request):
    return render(request,"../Templates/index.html")

def legales(request):
    return render(request, "../Templates/legales.html")
#----------------------------------------------------------------
#        ACERCA DE MI
#----------------------------------------------------------------
def acercaDeMi(request):
    return render(request,"../Templates/acercaDeMi.html")
#----------------------------------------------------------------
#        REGISTRO USUARIOS
#----------------------------------------------------------------
def registro(request):
    if request.method=="POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "../Templates/index.html", {"mensaje": f"Usuario {username} creado!"})
        else:
            return render(request, "../Templates/registro.html", {"form": form, "mensaje": "Error al crear"})
    else: 
        form = RegistroUsuarioForm()
        return render(request, "../Templates/registro.html", {"form": form})
#----------------------------------------------------------------
#        LOGIN USUARIOS
#----------------------------------------------------------------
def login_usuario(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            usuario=informacion["username"]
            clave=informacion["password"]
            user=authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request, "../Templates/index.html", {"mensaje": f"Hola de nuevo {usuario} ! 😀"})
            else:
                return render(request, "../Templates/login.html", {"form": form, "mensaje": "Usuario o contraseña incorrectos"})
        else:
            return render(request, "../Templates/login.html", {"form": form, "mensaje": "Usuario o contraseña incorrectos"})
    else:
        form= AuthenticationForm()
        return render(request, "../Templates/login.html", {"form": form})
#----------------------------------------------------------------
#        EDITAR USUARIOS
#----------------------------------------------------------------
@login_required
def editarUsuario(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST, request.FILES)
        if form.is_valid():
            informacion=form.cleaned_data
            usuario.username=informacion["username"]
            usuario.email=informacion["email"]
            usuario.password1=informacion["password1"]
            usuario.password2=informacion["password2"]
            usuario.save()
            return render(request, "../Templates/index.html", {"mensaje":f"Usuario {usuario.username} fue modificado con exito!"})
        else:
            return render(request, "../Templates/editarUsuario.html",{"form": form})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "../Templates/editarUsuario.html", {"form": form})
#----------------------------------------------------------------
#        VER PERFIL DE USUARIO
#----------------------------------------------------------------
@login_required
def verPerfil(request):
    usuario=request.user
    username=usuario.username
    email=usuario.email
    perfiles=CrearPerfil.objects.all()
    try:
        if len(perfiles)!=0:
            for perfil in perfiles:
                if perfil.pertenece == usuario:
                    link=perfil.link
                    acercademi=perfil.acercademi
                    imagen=perfil.imagen.url
                    sinperfil=False
                    return render(request, "../Templates/verPerfil.html", {"username": username,"email":email,"link":link,"acercademi":acercademi,"imagen":imagen,"sinperfil":sinperfil})
            else:
                sinperfil=True
                return render(request, "../Templates/verPerfil.html", {"username": username,"email":email,"sinperfil":sinperfil})
        else:
                sinperfil=True
                return render(request, "../Templates/verPerfil.html", {"username": username,"email":email,"sinperfil":sinperfil})
    except:
        sinperfil=True
        return render(request, "../Templates/verPerfil.html", {"username": username,"email":email,"sinperfil":sinperfil})

#----------------------------------------------------------------
#        CREAR PERFIL
#----------------------------------------------------------------
@login_required
def crearPerfil(request):
    if request.method=="POST":
        form = CrearPerfilForm(request.POST, request.FILES)
        if form.is_valid():
            informacion=form.cleaned_data
            link=informacion["link"]
            acercademi=informacion["acercademi"]
            imagen=informacion["imagen"]
            perfil=CrearPerfil(pertenece=request.user,link=link,acercademi=acercademi,imagen=imagen)
            perfil.save()
            return render(request, "../Templates/index.html", {"mensaje": f"Perfil creado!"})
        else:
            return render(request, "../Templates/crearPerfil.html", {"form": form, "mensaje": "Error al crear"})
    else: 
        perfiles=CrearPerfil.objects.all()
        if len(perfiles)!=0:
            for perfil in perfiles:
                if perfil.pertenece == request.user:
                    return render(request, "../Templates/index.html", {"mensaje":"UD ya tiene un perfil"})
                else:
                    form = CrearPerfilForm()
                    return render(request, "../Templates/crearPerfil.html", {"form": form})
        else:
            form = CrearPerfilForm()
            return render(request, "../Templates/crearPerfil.html", {"form": form})
#----------------------------------------------------------------
#        EDITAR PERFIL
#----------------------------------------------------------------

@login_required
def editarPerfil(request):
    perfil=CrearPerfil.objects.get(pertenece=request.user)
    if request.method=="POST":
        form=EditarPerfilForm(request.POST, request.FILES)
        if form.is_valid():
            informacion=form.cleaned_data
            perfil.link=informacion["link"]
            perfil.acercademi=informacion["acercademi"]
            perfil.imagen=informacion["imagen"]
            perfil.save()
            return render(request, "../Templates/index.html", {"mensaje":"Perfil modificado!"})
        else:
            return render(request, "../Templates/editarPerfil.html",{"form": form})
    else:
        form=EditarPerfilForm()
        return render(request, "../Templates/editarPerfil.html", {"form": form})
#----------------------------------------------------------------
#        PARA AGREGAR-EDITAR AVATAR
#----------------------------------------------------------------
@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "../Templates/index.html", {"mensaje": "Avatar modificado con exito"})
        else:
            return render(request, "../Templates/agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje": "Error al cargar el archivo"})
    else:
        form=AvatarForm()
        return render(request, "../Templates/agregarAvatar.html", {"form": form, "usuario": request.user})
#----------------------------------------------------------------
#        PARA MOSTRAR AVATAR
#----------------------------------------------------------------

def mostrarAvatar(request):#DRY DRY DRY
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar="../ProFinal/profinal/media/avatars/icons8-futurama-fry-64_1.png"
    return avatar

#----------------------------------------------------------------
#        PARA POSTEAR
#----------------------------------------------------------------
@login_required
def crearPost(request):
    if request.method=="POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            informacion=form.cleaned_data
            titulo=informacion["titulo"]
            subtitulo=informacion["subtitulo"]
            contenido=informacion["contenido"]
            imagen=informacion["imagen"]
            creado_el=informacion["creado_el"]
            posteo=CrearPost(titulo=titulo,subtitulo=subtitulo,contenido=contenido,imagen=imagen,autor=request.user,creado_el=creado_el,modificadoEl=creado_el)
            posteo.save()
            return render(request, "../Templates/index.html", {"mensaje": f"Post '{titulo}' creado!"})
        else:
            return render(request, "../Templates/crearPost.html", {"form": form, "mensaje": "UPS! ocurrio un error al crear el post, por favor verificar los campos"})
    else:
        form= PostForm()
        return render(request, "../Templates/crearPost.html", {"form": form})
#----------------------------------------------------------------
#        PARA BUSCAR POSTS
#----------------------------------------------------------------
@login_required
def buscarPost(request):
    return render(request, "../Templates/buscarPost.html")

@login_required
def buscar(request):
    titulo= request.GET["titulo"]
    if titulo!="":
        posts= CrearPost.objects.filter(titulo__icontains=titulo).order_by('-creado_el')#ver el mas reciente
        if len(posts)!=0:
            return render(request, "../Templates/resultadoBuscador.html", {"posts": posts})
        else:
            return render(request, "../Templates/buscarPost.html",{"mensaje":"No se encontraron coincidencias 🤖"})
    else:
        return render(request, "../Templates/buscarPost.html")

@login_required
def resultadoBuscador(request):
    return render(request, "../Templates/resultadoBuscador.html")
#----------------------------------------------------------------
#        PARA VER POSTS
#----------------------------------------------------------------
@login_required
def verPost(request, id):
    post=CrearPost.objects.get(id=id)
    titulo=post.titulo
    subtitulo=post.subtitulo
    contenido=post.contenido
    imagen=post.imagen.url#NOLOCAMBIESLPQTRP!
    autor=post.autor
    creado_el=post.creado_el
    modificadoEl=post.modificadoEl
    return render(request, "../Templates/verPost.html", {"titulo":titulo,"subtitulo":subtitulo,"contenido":contenido,"imagen":imagen,"autor":autor,"creado_el":creado_el,"modificadoEl":modificadoEl})
#----------------------------------------------------------------
#        PARA VER TODOS LOS POSTS
#----------------------------------------------------------------
@login_required
def verTodos(request):
    usuario=request.user
    posts= CrearPost.objects.all().order_by('-creado_el')#ver el mas reciente
    if len(posts)!=0:
        return render(request, "../Templates/verTodos.html", {"posts": posts,"usuario":usuario})
    else:
        return render(request, "../Templates/verTodos.html", {"mensaje":"No se han creado aun"})
#----------------------------------------------------------------
#        PARA VER EDITAR LOS POSTS
#----------------------------------------------------------------
@login_required
def editarPost(request,id):
    usuario=request.user
    post=CrearPost.objects.get(id=id)
    if usuario == post.autor:
        if request.method=="POST":
            form=EditarPostForm(request.POST, request.FILES)
            if form.is_valid():
                informacion=form.cleaned_data
                post.titulo=informacion["titulo"]
                post.subtitulo=informacion["subtitulo"]
                post.contenido=informacion["contenido"]
                post.imagen=informacion["imagen"]
                post.modificadoEl=informacion["modificadoEl"]
                post.save()
                return render(request, "../Templates/index.html",{"mensaje": "Posteo editado con exito!👍"})
            else:
                return render(request, "../Templates/editarPost.html",{"form":form,"id": id,"mensaje":"Ocurrio un error al editar"})
        else:
            form=EditarPostForm(initial={"titulo":post.titulo,"subtitulo":post.subtitulo,"contenido":post.contenido,"imagen":post.imagen})
            return render(request, "../Templates/editarPost.html", {"form": form, "id": id})#no borres el ID pajero
    else:
        return render(request,"../Templates/index.html",{"mensaje":"No tenes permiso para esto🚫"})
#----------------------------------------------------------------
#                  PARA ELIMINAR EL POST
#----------------------------------------------------------------
@login_required
def eliminarPost(request, id):
    post=CrearPost.objects.get(id=id)
    usuario=request.user
    if usuario == post.autor:
        post.delete()
        posts=CrearPost.objects.all().order_by('-creado_el')#ver el mas reciente
        return render(request, "../Templates/verTodos.html", {"posts": posts,"usuario":usuario})
    else:
        return render(request,"../Templates/index.html",{"mensaje":"No tenes permiso para esto🚫"})
#----------------------------------------------------------------
#                  LISTADO DE MIS POSTS
#----------------------------------------------------------------
@login_required
def misPosts(request):
    usuario=request.user
    posts= CrearPost.objects.filter(autor=usuario).order_by('-creado_el')#ver el mas reciente
    if len(posts)!=0:
        return render(request, "../Templates/misPosts.html", {"posts": posts,"usuario":usuario})
    else:
        return render(request, "../Templates/verTodos.html", {"mensaje":"No se han creado aun"})
