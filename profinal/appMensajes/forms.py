from django import forms
from .models import CrearMensaje, LEIDO_CHOICES
import datetime

class MensajeForm(forms.Form):

    receptor=forms.CharField(label="Receptor",max_length=30)
    cuerpo=forms.CharField(label="Cuerpo",max_length=50)
    fechaEnvio=forms.DateTimeField(label="Fecha",initial=datetime.datetime.now)

class VerMensajeForm(forms.Form):
    
    emisor=forms.CharField(label="Emisor",max_length=30,widget=forms.TextInput(attrs={'readonly':'readonly'}))
    cuerpo=forms.CharField(label="Cuerpo",max_length=50,widget=forms.TextInput(attrs={'readonly':'readonly'}))
    fechaEnvio=forms.DateTimeField(label="Fecha",initial=datetime.datetime.now,widget=forms.TextInput(attrs={'readonly':'readonly'}))
    leido=forms.ChoiceField(choices=LEIDO_CHOICES, required=True)

    class Meta:
        model= CrearMensaje
        fields=["emisor","cuerpo","leido"]
        help_text= {k:"" for k in fields}

class MensajeYaLeidoForm(forms.Form):
    emisor=forms.CharField(label="Emisor",max_length=30,disabled=True)
    cuerpo=forms.CharField(label="Cuerpo",max_length=50,disabled=True)
    fechaEnvio=forms.DateTimeField(label="Fecha",initial=datetime.datetime.now,disabled=True)


class ResponderMensaje(forms.Form):
    pass
