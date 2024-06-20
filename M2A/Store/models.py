from django.db import models

# Create your models here.

class Juego(models.Model):
    idJuego       = models.IntegerField(primary_key=True)
    nombre        = models.CharField(max_length=20)
    desarrollador = models.CharField(max_length=50)
    descripcion   = models.CharField(max_length=50)
    precio        = models.IntegerField()
    stock         = models.IntegerField()
    clave         = models.FileField(upload_to='juegos/claves_zip/',null= False)
    linkYoutube   = models.CharField(max_length=60)
    tipoClave     = models.CharField(max_length=40)


class Serie(models.Model):
    idSerie       = models.IntegerField(primary_key=True)
    nombre        = models.CharField(max_length=20)
    descripcion   = models.CharField(max_length=50)
    precio        = models.IntegerField()
    stock         = models.IntegerField()
    clave         = models.FileField(upload_to='series/claves_zip/',null= False)
    categoria     = models.ForeignKey('categoriaSerie', on_delete=models.CASCADE)    
    linkYoutube   = models.CharField(max_length=60)

class imagenSerie (models.Model):
    idSerie       = models.ForeignKey('Serie', on_delete=models.CASCADE)    
    idImagen      = models.IntegerField(primary_key=True)
    imagen        = models.ImageField(upload_to='series/imagenes/',null= False)

class categoriaSerie (models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)