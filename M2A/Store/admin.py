from django.contrib import admin
from .models import Juego, Serie, imagenSerie, categoriaSerie, imgJuegos, tipoClave, nivelEducacional, Usuario, Region

# Register your models here.
admin.site.register(Juego)
admin.site.register(Serie)
admin.site.register(Usuario)
admin.site.register(imagenSerie)
admin.site.register(Region)
admin.site.register(imgJuegos)
admin.site.register(categoriaSerie)
admin.site.register(tipoClave)
admin.site.register(nivelEducacional)