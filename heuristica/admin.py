from django.contrib import admin

# Register your models here.

from heuristica.models import Perfil
from heuristica.models import Juegos

admin.site.register(Perfil)
admin.site.register(Juegos)
