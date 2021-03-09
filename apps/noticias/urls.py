from django.urls import  path

from apps.noticias import views

urlpatterns = [
    path('', views.NoticiaListView.as_view(), name="noticia-list"),
    path('<int:pk>', views.NoticiaDetailView.as_view(), name='noticia-detail'),
]
