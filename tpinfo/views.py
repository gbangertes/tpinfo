from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def busqueda(request):
    return render(request, 'busqueda.html')
