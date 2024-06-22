from django.shortcuts import render
from .models import Juego
from M2A.settings import MEDIA_URL

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
