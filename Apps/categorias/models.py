from django.db import models

# Create your models here.
class Categoria(models.Model):
    id=models.AutoField(primary_key=True)
    tipocategoria=models.CharField(max_length=30)
    resumen=models.CharField(max_length=500)