from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import datetime
from ckeditor.widgets import CKEditorWidget
# Create your models here. class
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
    class meta:
        verbose_name_plural = 'Avatares'
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
class CrearPost(models.Model):
    
    titulo=models.CharField(max_length=30)
    subtitulo=models.CharField(max_length=30)
    contenido=RichTextUploadingField()
    imagen=models.ImageField(upload_to="ImagenPost")
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    creado_el=models.DateTimeField()
    modificadoEl=models.DateTimeField()
    
    
    
    class meta:
        verbose_name_plural = 'Crear Posteos'
    
    def __str__(self):
        return self.titulo
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
class CrearPerfil(models.Model):
    
    pertenece=models.ForeignKey(User, on_delete=models.CASCADE)
    link=models.URLField()
    acercademi=models.CharField(max_length=100)
    imagen=models.ImageField(upload_to="ImagenPerfil")
    
    class meta:
        verbose_name_plural = 'Perfiles'
    
    def __str__(self):
        return str(self.pertenece)
