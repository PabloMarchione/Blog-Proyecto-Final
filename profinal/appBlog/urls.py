from django.urls import path 
from .views import *
from django.contrib.auth.views import LogoutView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


urlpatterns = [
    path("", index, name="index"),
    path("legales/", legales, name="legales"),
    path("acercaDeMi/", acercaDeMi, name ="acercaDeMi"),
    
    path("registro/", registro, name="registro"),
    path("login/", login_usuario, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    
    path("crearPerfil/", crearPerfil, name="crearPerfil"),
    path("verPerfil/", verPerfil, name="verPerfil"),
    path("editarPerfil/", editarPerfil, name="editarPerfil"),
    
    path("editarUsuario/", editarUsuario, name="editarUsuario"),
    path("agregarAvatar/", agregarAvatar, name="agregarAvatar"),
    
    path("crearPost/", crearPost, name="crearPost"),
    path("verPost/<id>", verPost, name="verPost"),
    path("verTodos/", verTodos, name="verTodos"),
    path("editarPost/<id>", editarPost, name="editarPost"),
    path("eliminarPost/<id>", eliminarPost, name="eliminarPost"),
    path("misPosts/", misPosts, name="misPosts"),
    
    path("buscarPost/", buscarPost, name="buscarPost"),
    path("buscar/", buscar, name="buscar" ),
    path("resultadoBuscador/", resultadoBuscador, name="resultadoBuscador"),
    
    
]
