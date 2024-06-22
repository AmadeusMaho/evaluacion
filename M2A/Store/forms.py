from django import forms
from django.forms import ModelForm

from .models import Juego


class juegoForm(ModelForm):
    class Meta:
        model = Juego
        fields= "__all__"
