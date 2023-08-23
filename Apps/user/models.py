from django.db import models

# Create your models here.
from xmlrpc.client import boolean
from Apps.preguntaS.models import Pregunta


# Create your models here.
class User(models.Model):
    Nombre=models.CharField(max_length=50)
    Correo=models.EmailField(max_length=50)
    Password=models.CharField(max_length=50)
    Answer=models.CharField(max_length=50)
    IdRespuesta=models.ForeignKey(Pregunta,on_delete=models.CASCADE,null=True, blank=True)