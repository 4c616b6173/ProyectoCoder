from django.db import models

# Create your models here.
class curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Profesor(models.Model):
    # CharField = campo de texto
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    profesion = models.CharField(max_length=200)
    # EmailField = campo de email
    email = models.EmailField(max_length=200)
    # Hay más tipos de campos: Integer (números enteros), Date (fecha), etc...


class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    # Podemos crearles __str__ como cualquier clase
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=200)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()