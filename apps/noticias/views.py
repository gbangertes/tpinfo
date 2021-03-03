from django.shortcuts import render
from .models import Noticia

# Create your views here.

def recientes(request):
    recientes = Noticia.objects.all().reverse()[:10]
    ctx = {}
    ctx["noticias"] = recientes
    return render(request, "recientes.html", ctx)
