from django.shortcuts import render

# Create your views here.

def registro(request):
    return render(request, 'registro.html')

def login(request):
    return render(request, 'login2.html')
