from django.db import models

from xmlrpc.client import boolean
from Apps.user.models import User
from Apps.libro.models import libro


# Create your models here.
class Opinion(models.Model):
    nombreUser=models.CharField(max_length=30)
    calificacion=models.IntegerField()
    descripcion=models.CharField(max_length=250)
    idUser=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    idLibro=models.ForeignKey(libro,on_delete=models.CASCADE,null=True, blank=True)
    date=models.CharField(max_length=30)