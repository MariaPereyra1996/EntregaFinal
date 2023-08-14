from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Suscripcion(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

class Servicios(models.Model):
    nombre=models.CharField(max_length=50)
    encargado=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}, {self.encargado}"

class Clientes(models.Model):
    nombre=models.CharField(max_length=50)
    servicio_contratado=models.CharField(max_length=50)
    email=models.EmailField()

class Avatar(models.Model):
    imagen=models.ImageField(upload_to="avatares")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user} [{self.imagen}]"
    
class Oficinas(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)

class Eventos(models.Model):
    nombre=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)
    
    
    
