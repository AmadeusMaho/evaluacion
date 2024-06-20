from django.shortcuts import render

def principal(request):
    return render(request, 'principal.html', {})

def carrito(request):
    return render(request, 'carrito.html', {})
# Create your views here.

def juego(request):
    return render(request, 'juegoplantilla.html', {})

def plantilla(request):
    return render(request, 'plantilla_base.html', {})

def registro(request):
    return render(request, 'Login.html', {})

def registrarJuego(request):
    return render(request, 'registroJuegos.html', {})

def registrarSerie(request):
    return render(request, 'registroSeries.html', {})
