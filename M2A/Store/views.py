from django.shortcuts import render
from .models import Juego,tipoClave
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
        imagen        = request.FILES['imagen']
        ytVidId       = request.POST['link']
        precio        = request.POST['precio']
        stock         = request.POST['stock']
        clave         = request.FILES['archivo']
        
        #convertir idjuego en un string para comparar
        str(idJuego)
        if 'enviarJuego' in request.POST:
            if idJuego == "0":
                 Juego.objects.create(
                    nombre = nombre,
                    desarrollador = desarrollador,
                    descripcion = descripcion,
                    imagen = imagen,
                    ytVidId = ytVidId,
                    precio = precio,
                    stock = stock,
                    clave = clave,
                    tipoClave = tipoClave.objects.get(idTipo=request.POST['tipoClave'])
                    )
            else:
                juego = Juego.objects.get(idJuego = request.POST['txtId'])
                juego.nombre = nombre
                juego.desarrollador = desarrollador
                juego.descripcion = descripcion
                juego.imagen = imagen
                juego.ytVidId = ytVidId
                juego.precio = precio
                juego.stock = stock
                juego.clave = clave
                juego.tipoClave = tipoClave.objects.get(idTipo=request.POST['tipoClave'])
                juego.save()
                
    context['juegos'] = Juego.objects.all()
    return render(request, 'listadoJuegos.html', context)


def modificarJuego(request, idJuego):
    juego = Juego.objects.get(idJuego = idJuego)
    tipoClaves = tipoClave.objects.all()
    context = {
    'juego': juego,
    'tipoClaves': tipoClaves,
    }
    return render(request, 'registroJuegos.html', context)