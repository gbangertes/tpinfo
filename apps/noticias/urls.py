from django.urls import  path

from apps.noticias import views

urlpatterns = [
    path('', views.NoticiaListView.as_view(), name="noticia-list"),
    path('<int:pk>/', views.NoticiaDetailView.as_view(), name='noticia-detail'),
    path('nueva/', views.NoticiaCreate.as_view(), name="nueva-noticia"),
    #path('<int:pk>/comentarios/', views.ComentarioCreate.as_view(), name='noticia-comentario'),
    path('<int:pk>/nuevo_comentario/', views.ComentarioCreate.as_view(), name="nuevo-comentario"),
    path('categorias/', views.CategoriaListView.as_view(), name="categoria-list"),
    path('categorias/<int:pk>/', views.FiltroNoticias.as_view(), name='filtro-categoria'),
    path('<int:pk>/borrar_noticia/', views.NoticiaDelete.as_view(), name='noticia-delete'),
    path('<int:pk>/borrar_comentario/', views.ComentarioDelete.as_view(), name='comentario-delete'),
    path('<int:pk>/editar_noticia/', views.NoticiaUpdate.as_view(), name='noticia-update'),
    path('<int:pk>/editar_comentario/', views.ComentarioUpdate.as_view(), name='comentario-update'),
    path(r'^busqueda/$', views.BusquedaNoticia.as_view(), name='busqueda'),
]
