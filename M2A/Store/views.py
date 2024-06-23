from django.shortcuts import render, redirect
from .models import Juego, Carrito, tipoClave, Serie, imagenSerie,categoriaSerie, imgJuegos, Usuario, Region, nivelEducacional
from M2A.settings import MEDIA_URL
from django.contrib.auth.decorators import login_required
from .forms import juegoForm
<<<<<<< HEAD
from .forms import customLoginForm
from django.contrib.auth.views import LoginView,LogoutView



=======
import re
>>>>>>> b04b2f1b94d33377cf77115163770148948a03b5

def principal(request):
    return render(request, 'principal.html', {})

def carrito(request):
    return render(request, 'carrito.html', {})
# Create your views here.

def juego(request):
    return render(request, 'juegoplantilla copy.html', {})

def registroUsuarios(request):
    regiones = Region.objects.all()
    nivelesEducacionales = nivelEducacional.objects.all()
    context = {
    'regiones': regiones,
    'nivelesEducacionales': nivelesEducacionales,
    }
    return render(request, 'registroUsuarios.html', context)

def registroJuegos(request):
    tipoClaves = tipoClave.objects.all()

    context = {
    'tipoClaves': tipoClaves
    }
    return render(request, 'registroJuegos.html', context)

def registroSeries(request):
    categorias = categoriaSerie.objects.all()

    context = {
    'categorias': categorias
    }
    return render(request, 'registroSeries.html', context)

def verJuego(request, idJuego):
    juego = Juego.objects.get(idJuego = idJuego)
    capturas = imgJuegos.objects.filter(idJuego=juego)
    return render(request, 'juegoplantilla.html', {'juego': juego, 'capturas': capturas})

def verJuegosPrincipal(request):
    juegos = Juego.objects.all()
    context = {
    'juegos': juegos,
    'MEDIA_URL': MEDIA_URL 
    }
    return render(request, 'principal.html', context)

def plantilla(request):
    return render(request, 'plantilla_base.html', {})

@login_required
def agregarJuegoCarro(request, idJuego):
    context = {}
    try:
        usuario = request.user
        item = Juego.objects.get(idJuego = idJuego)
        carro, creado = Carrito.objects.get_or_create(usuario=usuario)
        carro.juegos.add(item)
        context['exito'] = 'Se agregó el producto'
    except:
        context['Error'] = 'Error al agregar el producto'
    return redirect(verCarro)

@login_required
def verCarro(request):
    context = {}
    try:
        usuario = request.user
        listado = Carrito.objects.get(usuario = usuario)
        listado = listado.juegos.all
        context = {"listado": listado}
    except:
        context = {}
    return render(request, 'carrito.html', context)

@login_required
def eliminarJuegoCarro(request, idJuego):
    context = {}
    try:
        usuario = request.user
        listado = Carrito.objects.get(usuario = usuario)
        juego = listado.juegos.get(idJuego = idJuego)
        listado = listado.juegos
        listado.remove(juego)
        context['exito'] = 'Producto eliminado del carrito'
    except:
        context['error'] = 'Error al eliminar el producto'
    return redirect(verCarro)

# juegos:

def listadoJuegos(request):
    juegos = Juego.objects.all()
    tipoClaves = tipoClave.objects.all()
    context = {
    'juegos': juegos,
    'tipoClaves': tipoClaves 
    }
    return render(request, 'listadoJuegos.html', context)

def eliminarJuego(request, idJuego):
    context = {}
    try:
        juego = Juego.objects.get(idJuego = idJuego)
        juego.delete()
        context['exito'] = 'Juego eliminado con éxito'
    except:
        context['error'] = 'Error al eliminar el juego'
    
    juegos = Juego.objects.all()
    context['juegos'] = juegos
    return render(request, 'listadoJuegos.html', context)

def subirJuego(request):
    context = {'form': juegoForm()}
    if request.method == 'POST':
        idJuego       = request.POST['txtId']
        nombre        = request.POST['nombre']
        desarrollador = request.POST['titulo']
        descripcion   = request.POST['descripcion']
        ytVidId       = request.POST['link']
        precio        = request.POST['precio']
        stock         = request.POST['stock']

        # buscar youtube id
        m = re.search(r"([\d\w]{11})", ytVidId)
        ytVidId = m.group()
        
        #convertir idjuego en un string para comparar
        str(idJuego)
        if 'enviarJuego' in request.POST:
            if idJuego == "0":
                 juego1= Juego.objects.create(
                    nombre = nombre,
                    desarrollador = desarrollador,
                    descripcion = descripcion,
                    imagen = request.FILES['imagen'],
                    ytVidId = ytVidId,
                    precio = precio,
                    stock = stock,
                    clave = request.FILES['archivo'],
                    tipoClave = tipoClave.objects.get(idTipo=request.POST['tipoClave'])
                    )
                 if request.FILES.getlist('captura'):
                    capturas = request.FILES.getlist('captura')
                    for imagen in capturas:
                        imgJuegos.objects.create(
                            idJuego = juego1,
                            imagen = imagen
                        )
            else:
                juego = Juego.objects.get(idJuego = request.POST['txtId'])
                juego.nombre = nombre
                juego.desarrollador = desarrollador
                juego.descripcion = descripcion
                juego.ytVidId = ytVidId
                juego.precio = precio
                juego.stock = stock
                juego.tipoClave = tipoClave.objects.get(idTipo=request.POST['tipoClave'])
                if 'imagen' in request.FILES:
                    juego.imagen = request.FILES['imagen']
                if 'archivo' in request.FILES:
                    juego.clave = request.FILES['archivo']
                juego.save()
                if request.FILES.getlist('captura'):
                    capturas = request.FILES.getlist('captura')
                    capturas_old = imgJuegos.objects.filter(idJuego=juego)
                    for old in capturas_old:
                        old.delete()
                    for imagen in capturas:
                        imgJuegos.objects.create(
                            idJuego = juego,
                            imagen = imagen
                        )
                
    #context['juegos'] = Juego.objects.all()
    #return render(request, 'listadoJuegos.html', context)
    return redirect(listadoJuegos)


def modificarJuego(request, idJuego):
    juego = Juego.objects.get(idJuego = idJuego)
    tipoClaves = tipoClave.objects.all()
    capturas = imgJuegos.objects.filter(idJuego=juego)
    urlCapturas = ""
    for i in capturas:
        urlCapturas += i.imagen.url + " "
    context = {
    'juego': juego,
    'tipoClaves': tipoClaves,
    'capturas' : capturas,
    'urlCapturas' : urlCapturas
    }
    return render(request, 'registroJuegos.html', context)


#series:

def listadoSeries(request):
    series = Serie.objects.all()
    categorias = categoriaSerie.objects.all()
    context = {
    'series': series,
    'categorias': categorias 
    }
    return render(request, 'listadoSeries.html', context)


def eliminarSerie(request, idSerie):
    context = {}
    try:
        serie = Serie.objects.get(idSerie = idSerie)
        serie.delete()
        context['exito'] = 'Serie eliminada con éxito'
    except:
        context['error'] = 'Error al eliminar la Serie'
    
    serie = Serie.objects.all()
    context['serie'] = serie
    return render(request, 'listadoSeries.html', context)


def subirSerie(request):
    context = {}
    if request.method == 'POST':
        
        idSerie         = request.POST['txtId']
        nombre          = request.POST['titulo']
        estudio         = request.POST['estudio']
        descripcion     = request.POST['descripcion']
        precio          = request.POST['precio']
        stock           = request.POST['stock']
        ytVidId         = request.POST['link']
        fechalanz       = request.POST['lanzamiento']
        
        #convertir idserie en un string para comparar
        str(idSerie)
        if 'enviarSerie' in request.POST:
            if idSerie == "0":
                 Serie.objects.create(
                    nombre = nombre,
                    estudio = estudio,
                    descripcion = descripcion,
                    imagen = request.FILES['imagen'],
                    ytVidId = ytVidId,
                    precio = precio,
                    stock = stock,
                    clave = request.FILES['archivo'],
                    fechalanz = fechalanz,
                    categoria = categoriaSerie.objects.get(idCategoria=request.POST['categoria'])
                    )
            else:
                serie = Serie.objects.get(idSerie = request.POST['txtId'])
                serie.nombre = nombre
                serie.estudio = estudio
                serie.descripcion = descripcion
                serie.ytVidId = ytVidId
                serie.precio = precio
                serie.stock = stock
                serie.fechalanz = fechalanz
                serie.categoria = categoriaSerie.objects.get(idCategoria=request.POST['categoria'])
                if 'imagen' in request.FILES:
                    serie.imagen = request.FILES['imagen']
                if 'archivo' in request.FILES:
                    serie.clave = request.FILES['archivo']
                serie.save()
                
    context['series'] = Serie.objects.all()
    return render(request, 'listadoSeries.html', context)


def modificarSerie(request, idSerie):
    serie = Serie.objects.get(idSerie = idSerie)
    categorias = categoriaSerie.objects.all()
    context = {
    'serie': serie,
    'categorias': categorias,
    }
    return render(request, 'registroSeries.html', context)

#usuarios:

def listadoUsuarios(request):
    usuario = Usuario.objects.all()
    regiones = Region.objects.all()
    nivelesEducacionales = nivelEducacional.objects.all()
    context = {
    'usuario': usuario,
    'regiones': regiones,
    'nivelesEducacionales': nivelesEducacionales,
    }
    return render(request, 'listadoUsuarios.html', context)


def eliminarUsuario(request, idUsuario):
    context = {}
    try:
        usuario = Usuario.objects.get(idUsuario = idUsuario)
        usuario.delete()
        context['exito'] = 'Usuario eliminado con éxito'
    except:
        context['error'] = 'Error al eliminar el Usuario'
    
    usuarios = Usuario.objects.all()
    context['usuario'] = usuarios
    return render(request, 'listadoUsuarios.html', context)


def registrarse(request):
    context = {}
    if request.method == 'POST':
        
        idUsuario = request.POST['txtId']
        nombre    = request.POST['txtNombre']
        apellido  = request.POST['txtApellido']
        rut       = request.POST['txtRut']
        email     = request.POST['txtEmail']
        telefono  = request.POST['txtTelefono']
        fechaNac  = request.POST['edad']
        #convertir idusuario en un string para comparar
        str(idUsuario)
        if 'enviarRegistro' in request.POST:
            if idUsuario == "0":
                 Usuario.objects.create(
                    nombre = nombre,
                    apellido = apellido,
                    rut = rut,
                    email = email,
                    telefono = telefono,
                    region = Region.objects.get(idRegion=request.POST['txtRegion']),
                    nivelEd = nivelEducacional.objects.get(idEducacion=request.POST['txtNvlEducacional']),
                    fechaNac = fechaNac
                    )
            else:
                usuario = Usuario.objects.get(idUsuario = request.POST['txtId'])
                usuario.nombre = nombre
                usuario.apellido = apellido
                usuario.rut = rut
                usuario.email = email
                usuario.telefono = telefono
                usuario.fechaNac = fechaNac
                usuario.region = Region.objects.get(idRegion=request.POST['txtRegion'])
                usuario.nivelEd = nivelEducacional.objects.get(idEducacion=request.POST['txtNvlEducacional'])
                usuario.save()
                
    context['usuario'] = Usuario.objects.all()
    return render(request, 'listadoUsuarios.html', context)

def modificarUsuario(request, idUsuario):
    usuario = Usuario.objects.get(idUsuario = idUsuario)
    nivelesEducacionales = nivelEducacional.objects.all()
    regiones = Region.objects.all()
    context = {
    'usuario': usuario,
    'nivelesEducacionales': nivelesEducacionales,
    'regiones': regiones,
    }
    return render(request, 'registroUsuarios.html', context)


class CustomLoginView(LoginView):
    template_name = 'login.html' 
    authentication_form = customLoginForm
    redirect_authenticated_user = True