from django.shortcuts import render

# Create your views here.
def recientes(request):
    return render(request, "recientes.html")
