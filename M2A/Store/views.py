from django.shortcuts import render

def menu(request):
    return render(request, 'plantillaBase.html', {})
# Create your views here.
