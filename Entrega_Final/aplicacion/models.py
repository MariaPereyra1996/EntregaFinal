from django.db import models

from django.db import models

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
    
