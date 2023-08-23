from django.db import models
from Apps.categorias.models import Categoria

# Create your models here.
class libro(models.Model):
    nombre=models.CharField(max_length=30)
    Autor=models.CharField(max_length=30)
    categoria=models.ForeignKey(Categoria,max_length=30,on_delete=models.CASCADE)
    calificacion=models.FloatField(max_length=30)
    resumen=models.TextField(max_length=500)
    file = models.ImageField(upload_to='images/')