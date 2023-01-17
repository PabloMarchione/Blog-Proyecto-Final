from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
import datetime
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *

#Estos los hace DJANGO unchained
#---------------------------------------------------------------------------------------------
class RegistroUsuarioForm(UserCreationForm):
    username= forms.CharField(label= "Nombre")
    email= forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label= "Confirmar contraseña", widget=forms.PasswordInput)
    
    
    class Meta:
        model= User
        fields=["username","email","password1","password2"]
        help_text= {k:"" for k in fields}
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
class UserEditForm(UserCreationForm):
    username= forms.CharField(label= "Nombre")
    email= forms.EmailField(label="Tu Email")
    password1= forms.CharField(label= "Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label= "Confirmar contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model= User
        
        fields=["username","email","password1","password2"]
        help_text= {k:"" for k in fields}
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
class CrearPerfilForm(forms.Form):
    
    link= forms.URLField()
    acercademi= forms.CharField(label="Acerca de mi",max_length=100)
    imagen= forms.ImageField(label="Imagen")
    
    class Meta:
        model= CrearPerfil
        fields=["link","acercademi","imagen"]
        help_text= {k:"" for k in fields}

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
class EditarPerfilForm(CrearPerfilForm):
    
    link= forms.URLField()
    acercademi= forms.CharField(label="Acerca de mi",max_length=100)
    imagen= forms.ImageField(label="Imagen")
    
    class Meta:
        model= CrearPerfil
        fields=["link","acercademi","imagen"]
        help_text= {k:"" for k in fields}
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
class AvatarForm(forms.Form):
    imagen=forms.ImageField(label=False)
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
class PostForm(forms.Form):
    titulo = forms.CharField(label="Titulo",max_length=30)
    subtitulo = forms.CharField(label="Subtitulo",max_length=30)
    contenido = forms.CharField(label="Contenido",widget=CKEditorUploadingWidget())
    imagen= forms.ImageField(label="Portada")
    creado_el = forms.DateTimeField(initial=datetime.datetime.now,widget=forms.TextInput(attrs={'readonly':'readonly'}))
    
    class Meta:
        model=CrearPost
        fields=["titulo","subtitulo","contenido","imagen","creado_el"]
        help_text= {k:"" for k in fields}
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
class EditarPostForm(forms.Form):
    titulo = forms.CharField(label="Titulo",max_length=30)
    subtitulo = forms.CharField(label="Subtitulo",max_length=30)
    contenido = forms.CharField(label="Contenido",widget=CKEditorUploadingWidget())
    imagen= forms.ImageField(label="Portada")
    modificadoEl = forms.DateTimeField(label="Editado el",initial=datetime.datetime.now,widget=forms.TextInput(attrs={'readonly':'readonly'}))