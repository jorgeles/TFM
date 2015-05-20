from django.contrib import admin

# Register your models here.

from heuristica.models import Perfil
from heuristica.models import Juegos
from heuristica.models import Heuristica
from heuristica.models import MiTest

admin.site.register(Perfil)
admin.site.register(Juegos)
admin.site.register(Heuristica)
admin.site.register(MiTest)