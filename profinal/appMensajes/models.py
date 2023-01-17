from django.db import models
from django.contrib.auth.models import User
# Create your models here.

LEIDO_CHOICES = [
    ("NO","no"),
    ("SI","si"),
]

class CrearMensaje(models.Model):
    
    creador=models.ForeignKey(User, on_delete=models.CASCADE)
    emisor=models.CharField(default="...", max_length=30)
    receptor=models.CharField(max_length=30)
    cuerpo=models.CharField(max_length=50)
    leido=models.CharField(max_length=10, choices= LEIDO_CHOICES, default="NO")
    fechaEnvio=models.DateTimeField()
    
    def __str__(self):
        return self.emisor