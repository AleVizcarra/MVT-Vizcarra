from pyexpat import model
from django.db import models

# Create your models here.

# La clase del modelo, deberá guardar mínimo:
# 1 número
# 1 cadena
# 1 fecha


class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
