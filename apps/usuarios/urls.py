from django.urls import  path

from apps.usuarios import views

urlpatterns = [
    path('registro/', views.Registro.as_view(), name="registro"),
    path('bienvenida/', views.bienvenida, name="bienvenida")
]
