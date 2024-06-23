from django.shortcuts import render, redirect
from .models import Juego, Carrito
from M2A.settings import MEDIA_URL
from django.contrib.auth.decorators import login_required

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
    return render(request, 'registroJuegos.html', {})

def registroSeries(request):
    return render(request, 'registroSeries.html', {})

def verJuego(request, idJuego):
    juego = Juego.objects.get(idJuego = idJuego)
    return render(request, 'juegoplantilla.html', {'juego':juego})

def verJuegosPrincipal(request):
    context = {}
    juegos = Juego.objects.all()
    context = {
    'juegos': juegos,
    'MEDIA_URL': MEDIA_URL  # Accedemos a MEDIA_URL desde settings
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
