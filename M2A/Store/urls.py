from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('principal', views.principal, name='principal'),
    path('carrito', views.carrito, name='carrito'),
    path('juego', views.juego, name='juego'),

]