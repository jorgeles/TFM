import datetime
from django.utils import timezone
from django.db import models

# Create your models here.

class Perfil (models.Model):
    id=models.AutoField(primary_key=True)
    propietario=models.CharField (max_length=200)
    nombre = models.CharField (max_length=200)
    disruptor = models.CharField (max_length=200)
    filantropo = models.CharField (max_length=200)
    socializador = models.CharField (max_length=200)
    jugador = models.CharField (max_length=200)
    logrador = models.CharField (max_length=200)
    espiritu = models.CharField (max_length=200)

class Juegos (models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField (max_length=200)
    propietario=models.CharField (max_length=200)
    aventuras=models.CharField (max_length=200)
    accion = models.CharField (max_length=200)
    fps = models.CharField (max_length=200)
    simulacion = models.CharField (max_length=200)
    plataformas = models.CharField (max_length=200)
    estrategia = models.CharField (max_length=200)
    deporte = models.CharField (max_length=200)
    motor = models.CharField (max_length=200)
    rol = models.CharField (max_length=200)
    sandbox = models.CharField (max_length=200)
    party = models.CharField (max_length=200)
    educativo = models.CharField (max_length=200)
    musical = models.CharField (max_length=200)

class Heuristica(models.Model):
    id=models.AutoField(primary_key=True)
    jugabilidad=models.CharField (max_length=2)
    propietario=models.CharField (max_length=200)
    nombre = models.CharField (max_length=200)
    comentario = models.CharField (max_length=2000)
    rango = models.CharField (max_length=20)
    elementos = models.CharField (max_length=20000)
    atributos = models.CharField (max_length=20000)
    comentarioVisible = models.CharField (max_length=2)

class MiTest(models.Model):
    id=models.AutoField(primary_key=True)
    propietario=models.CharField (max_length=200)
    nombre = models.CharField (max_length=200)
    titulo = models.CharField (max_length=200)
    seleccionados = models.CharField (max_length=200000)
    asignados = models.CharField (max_length=2000)
    comentarios = models.CharField (max_length=200000)


class Asignados(models.Model):
    id=models.AutoField(primary_key=True)
    propietario=models.CharField (max_length=200)
    creador=models.CharField (max_length=200)
    nombre = models.CharField (max_length=200)
    titulo = models.CharField (max_length=200)
    seleccionados = models.CharField (max_length=200000)
    idTest=models.CharField (max_length=200)
    respuestas=models.CharField (max_length=200000)

class Resultados(models.Model):
    id=models.AutoField(primary_key=True)
    propietario=models.CharField (max_length=200)
    idTest=models.CharField (max_length=200)
    respuestas=models.CharField (max_length=200000)
    seleccionados = models.CharField (max_length=200000)

