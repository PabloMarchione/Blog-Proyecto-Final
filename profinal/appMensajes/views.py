from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from appMensajes.forms import *

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

@login_required
def panelMensajes(request):
    return render(request,"../Templates/panelMensajes.html")

@login_required
def enviarMensaje(request):
    usuario=request.user
    if request.method=="POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            receptor=informacion["receptor"]
            cuerpo=informacion["cuerpo"]
            fechaEnvio=informacion["fechaEnvio"]
            mensaje=CrearMensaje(creador=request.user,emisor=request.user,receptor=receptor,cuerpo=cuerpo,fechaEnvio=fechaEnvio)
            existeUsuario = User.objects.filter(username__in=[receptor]).values()#alfin la puta madre
            if mensaje.receptor != usuario.username:
                if len(existeUsuario)!=0:
                        mensaje.save()
                        return render(request,"../Templates/panelMensajes.html",{"mensaje":"Enviado!!!"})
                else:
                    return render(request,"../Templates/enviarMensaje.html",{"form":form,"mensaje":"Destinatario invalido"})
            else:
                return render(request,"../Templates/enviarMensaje.html",{"form":form,"mensaje":"No podes mandarte mensajes a vos mismo giltrul"})  
        else:
            return render(request,"../Templates/enviarMensaje.html",{"form":form,"mensaje":"Algo Fallo!"})
    else:
        form=MensajeForm()
        return render(request,"../Templates/enviarMensaje.html",{"form":form})

@login_required
def bandejaEntrada(request):
    listado= CrearMensaje.objects.filter(receptor=request.user).values().order_by('-fechaEnvio')#ver el mas reciente
    if len(listado)!=0:
        return render(request,"../Templates/bandejaEntrada.html",{"listado":listado})
    else:
        return render(request,"../Templates/panelMensajes.html",{"mensaje":"No existen mensajes"})
    
@login_required
def bandejaSalida(request):
    listado= CrearMensaje.objects.filter(creador=request.user).values().order_by('-fechaEnvio')#ver el mas reciente
    if len(listado)!=0:
        return render(request,"../Templates/bandejaSalida.html",{"listado":listado})
    else:
        return render(request,"../Templates/panelMensajes.html",{"mensaje":"No existen mensajes"})
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
@login_required
def verMensaje(request,id):
        mensajito=CrearMensaje.objects.get(id=id)
        if mensajito.leido == "NO":
            if request.method=="POST":
                form=VerMensajeForm(request.POST)
                if form.is_valid():
                    info=form.cleaned_data
                    mensajito.emisor=info["emisor"]
                    mensajito.cuerpo=info["cuerpo"]
                    mensajito.fechaEnvio=info["fechaEnvio"]
                    mensajito.leido=info["leido"]
                    
                    mensajito.save()
                    return render(request, "../Templates/bandejaEntrada.html",{"mensaje": "Leido!"})
                else:
                    return render(request, "../Templates/verMensaje.html",{"form":form,"id": id,"mensaje":"Ocurrio un error leer"})
            else:
                form=VerMensajeForm(initial={"emisor":mensajito.emisor,"cuerpo":mensajito.cuerpo,"fechaEnvio":mensajito.fechaEnvio})
                return render(request, "../Templates/verMensaje.html", {"mensajito":mensajito,"form": form, "id": id})
        else:
            form=MensajeYaLeidoForm(initial={"emisor":mensajito.emisor,"cuerpo":mensajito.cuerpo,"fechaEnvio":mensajito.fechaEnvio})
            return render(request, "../Templates/verMensaje.html", {"mensajito":mensajito,"form": form, "id": id})
        
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------



