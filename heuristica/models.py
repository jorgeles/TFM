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

    
