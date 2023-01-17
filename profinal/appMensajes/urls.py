from django.urls import path 
from .views import *

urlpatterns = [
    path("panelMensajes/", panelMensajes, name="panelMensajes"),
    path("enviarMensaje/", enviarMensaje, name="enviarMensaje"),
    path("bandejaEntrada/", bandejaEntrada, name="bandejaEntrada"),
    path("bandejaSalida/", bandejaSalida, name="bandejaSalida"),
    
    path("verMensaje/<id>", verMensaje, name="verMensaje"),
    
]