from django.shortcuts import render
from django.views.generic import CreateView
from .models import Usuario
from django.urls import reverse_lazy
from .forms import Formulario_Alta_Usuario

# Create your views here.

class Registro(CreateView):
    model = "Usuario"
    form_class = Formulario_Alta_Usuario
    template_name = "usuarios/registro.html"
    success_url = reverse_lazy("bienvenida")

def bienvenida(request):
    return render(request,'usuarios/bienvenida.html')
