from django.contrib import admin
<<<<<<< HEAD
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
=======
from .models import Juego
from .models import tipoClave

# Register your models here.
admin.site.register(Juego)
admin.site.register(tipoClave)
>>>>>>> a367bca110a34edcbf3a146e1df7cabd7e72ee81
