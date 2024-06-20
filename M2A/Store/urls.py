from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('principal', views.principal, name='principal'),
    path('carrito', views.carrito, name='carrito'),
    path('juego', views.juego, name='juego'),
    path('plantilla', views.plantilla, name='plantilla'),
    path('registro', views.registro, name='registro'),
    path('registrarSerie', views.registrarSerie, name='registrarSerie'),
    path('registrarJuego', views.registrarJuego, name='registrarJuego')

]