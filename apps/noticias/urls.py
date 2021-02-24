from django.urls import  path

from apps.noticias import views

urlpatterns = [
    path('', views.recientes, name="recientes"),
]
