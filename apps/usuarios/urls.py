from django.urls import  path

from apps.usuarios import views

urlpatterns = [
    path('registro/', views.registro, name="registro"),
    # path('login/', views.login, name="login"),
]

