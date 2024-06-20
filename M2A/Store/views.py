from django.shortcuts import render

def principal(request):
    return render(request, 'principal.html', {})

def carrito(request):
    return render(request, 'carrito.html', {})
# Create your views here.

def juego(request):
    return render(request, 'juegoplantilla.html', {})

def login(request):
    return render(request, 'login.html', {})

def registroJuegos(request):
    return render(request, 'registroJuegos.html', {})

def registroSeries(request):
    return render(request, 'registroSeries.html', {})

def plantilla(request):
    return render(request, 'plantilla_base.html', {})
