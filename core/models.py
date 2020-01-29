from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

class Evento(models.Model):
    nombre = models.CharField(max_length=30,null=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,null=True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    lugar = models.CharField(max_length=30,null=True)
    direccion=models.CharField(max_length=30,null=True)
    fechaInicio= models.DateField(null=True)
    fechaFin= models.DateField(null=True)
    presencial= models.BooleanField(default=False,null=True)
