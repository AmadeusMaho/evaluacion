from django.db import models

# Create your models here.

class Juego(models.Model):
    idJuego       = models.IntegerField(primary_key=True)
    nombre        = models.CharField(max_length=20)
    desarrollador = models.CharField(max_length=50)
    descripcion   = models.CharField(max_length=550)
    imagen        = models.ImageField(upload_to='juegos/imagenes')
    ytVidId       = models.CharField(max_length=11, null=True)
    precio        = models.IntegerField()
    stock         = models.IntegerField()
    clave         = models.FileField(upload_to='juegos/archivos_zip/',null= False)
    tipoClave     = models.ForeignKey('tipoClave', on_delete=models.CASCADE)

class tipoClave(models.Model):
    idTipo        = models.IntegerField(primary_key=True)
    nombre        = models.CharField(max_length=20)

class imgJuegos(models.Model):
    idImg         = models.IntegerField(primary_key=True)
    idJuego       = models.ForeignKey('Juego', on_delete=models.CASCADE)
    imagen        = models.ImageField(upload_to='juegos/capturas')


class Serie(models.Model):
    idSerie       = models.IntegerField(primary_key=True)
    nombre        = models.CharField(max_length=20)
    descripcion   = models.CharField(max_length=550)
    precio        = models.IntegerField()
    imagen        = models.ImageField(upload_to='series/imagenes')
    stock         = models.IntegerField()
    clave         = models.FileField(upload_to='series/claves_zip/',null= False)
    categoria     = models.ForeignKey('categoriaSerie', on_delete=models.CASCADE)    
    ytVidId       = models.CharField(max_length=11)

class imagenSerie (models.Model):
    idSerie       = models.ForeignKey('Serie', on_delete=models.CASCADE)    
    idImagen      = models.IntegerField(primary_key=True)
    imagen        = models.ImageField(upload_to='series/imagenes/',null= False)

class categoriaSerie (models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)

class Usuario ( models.Model):
    idUsuario = models.IntegerField(primary_key=True)
    nombre    = models.CharField(max_length=20)
    apellido  = models.CharField(max_length=20)
    email  = models.EmailField(max_length=70)
    telefono = models.CharField(max_length=40)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)   
    nivelEducacional = models.ForeignKey('nivelEducacional', on_delete=models.CASCADE)   
    fechaNac = models.DateField()

class Region (models.Model):
    idRegion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=40)

class nivelEducacional(models.Model):
    idEducacion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60)