from django.contrib import admin

# Register your models here.

from heuristica.models import Usuario
from heuristica.models import Perfil

admin.site.register(Usuario)
admin.site.register(Perfil)
