from django.urls import  path

from apps.noticias import views

urlpatterns = [
    path('', views.NoticiaListView.as_view(), name="noticia-list"),
    path('<int:pk>', views.NoticiaDetailView.as_view(), name='noticia-detail'),
    path('nueva/', views.NoticiaCreate.as_view(), name="nueva-noticia"),
    #path('<int:pk>/comentarios/', views.ComentarioCreate.as_view(), name='noticia-comentario'),
    path('<int:pk>/nuevo_comentario/', views.ComentarioCreate.as_view(), name="nuevo-comentario"),
    	]
