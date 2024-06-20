from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('principal', views.principal, name='principal'),
    path('carrito', views.carrito, name='carrito'),
    path('juego', views.juego, name='juego'),
    path('login', views.login, name='login'),
    path('registroJuegos', views.registroJuegos, name='registroJuegos'),
    path('registroSeries', views.registroSeries, name='registroSeries'),
    path('plantilla', views.plantilla, name='plantilla'),

]