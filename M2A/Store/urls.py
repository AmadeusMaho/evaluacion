from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.principal, name='principal'),
    path('principal', views.verJuegosPrincipal, name='verJuegosPrincipal'),
    path('principal', views.principal, name='principal'),
    path('carrito', views.verCarro, name='carrito'),
    path('juego', views.juego, name='juego'),
    path('login', views.login, name='login'),
    path('registroJuegos', views.registroJuegos, name='registroJuegos'),
    path('registroSeries', views.registroSeries, name='registroSeries'),
    path('<int:idJuego>/', views.verJuego, name='verJuego'),
    path('plantilla', views.plantilla, name='plantilla'),
    path('agregarJuegoCarro/<int:idJuego>', views.agregarJuegoCarro, name='agregarJuegoCarro'),
    path('eliminarJuegoCarro/<int:idJuego>', views.eliminarJuegoCarro, name='eliminarJuegoCarro'),
    path('listadoJuegos', views.listadoJuegos, name='listadoJuegos'),
    path('eliminarJuego/<int:idJuego>', views.eliminarJuego, name='eliminarJuego'),
    path('registroJuegos/<int:idJuego>', views.modificarJuego, name='modificarJuego'),
    path('subirJuego', views.subirJuego, name='subirJuego'),
    path('listadoSeries', views.listadoSeries, name='listadoSeries'),
    path('eliminarSerie/<int:idSerie>', views.eliminarSerie, name='eliminarSerie'),
    path('registroSeries/<int:idSerie>', views.modificarSerie, name='modificarSerie'),
    path('subirSerie', views.subirSerie, name='subirSerie'),
]