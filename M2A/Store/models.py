from django.db import models

# Create your models here.

class Juego(models.Model):
    idJuego       = models.IntegerField(primary_key=True)
    nombre        = models.CharField(max_length=20)
    desarrollador = models.CharField(max_length=50)
    descripcion   = models.CharField(max_length=50)
    imagen        = models.ImageField(upload_to='juegos/imagenes')
    ytVidId       = models.CharField(max_length=11)
    precio        = models.IntegerField()
    stock         = models.IntegerField()
    clave         = models.FileField(upload_to='juegos/archivos_zip/',null= False)
    tipoClave     = models.ForeignKey('tipoClave', on_delete=models.CASCADE)

class tipoClave(models.Model):
    idTipo        = models.IntegerField(primary_key=True)
    nombre        = models.CharField(max_length=20)

class imgJuegos(models.Model):
    idImg         = models.IntegerField(primary_key=True)
    idJuego       = models.ForeignKey('Juego, on_delete=models.CASCADE')
    imagen        = models.ImageField(upload_to='juegos/capturas')