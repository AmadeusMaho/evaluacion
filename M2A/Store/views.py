from django.shortcuts import render, redirect
from .models import Juego, Carrito, tipoClave
from M2A.settings import MEDIA_URL
from django.contrib.auth.decorators import login_required
from .forms import juegoForm

def principal(request):
    return render(request, 'principal.html', {})

def carrito(request):
    return render(request, 'carrito.html', {})
# Create your views here.

def juego(request):
    return render(request, 'juegoplantilla copy.html', {})

def login(request):
    return render(request, 'login.html', {})

def registroJuegos(request):
    tipoClaves = tipoClave.objects.all()

    context = {
    'tipoClaves': tipoClaves
    }
    return render(request, 'registroJuegos.html', context)

def registroSeries(request):
    
    return render(request, 'registroSeries.html', {})

def verJuego(request, idJuego):
    juego = Juego.objects.get(idJuego = idJuego)
    return render(request, 'juegoplantilla.html', {'juego':juego})

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


def listadoJuegos(request):
    juegos = Juego.objects.all()
    return render(request, 'listadoJuegos.html', {'juegos':juegos})

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
    # captura de solicitud realizada por el usuario
    if request.method == 'POST':
        idJuego       = request.POST['txtId']
        nombre        = request.POST['nombre']
        desarrollador = request.POST['titulo']
        descripcion   = request.POST['descripcion']
        imagen        = request.FILES['imagen']
        ytVidId       = request.POST['link']
        precio        = request.POST['precio']
        stock         = request.POST['stock']
        clave         = request.FILES['archivo']
        tipoClave     = request.POST['tipoClave']
        if 'enviarJuego' in request.POST:
            juego = None
            if request.POST['txtId'] != "0":
                juego = Juego()
                juego.idJuego = idJuego
                juego.nombre = nombre
                juego.desarrollador = desarrollador
                juego.descripcion = descripcion
                juego.imagen = imagen
                juego.ytVidId = ytVidId
                juego.precio = precio
                juego.stock = stock
                juego.clave = clave
                juego.tipoClave = tipoClave
    context['juegos'] = Juego.objects.all()
    return render(request, 'listadoJuegos.html', context)
