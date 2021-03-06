from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Noticia, Categoria 
from apps.comentarios.models import Comentario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from django_filters.views import FilterView
from .filters import FiltroBusqueda
from .forms import NuevaNoticia, NuevoComentario, FormularioFecha


class NoticiaDetailView(generic.DetailView):
    model = Noticia


class NoticiaListView(generic.ListView):
    model = Noticia
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fecha'] = FormularioFecha
        return context


class NoticiaCreate(LoginRequiredMixin, CreateView):
    model = Noticia
    form_class = NuevaNoticia
    template_name = "noticias/nueva_noticia.html"
    success_url = reverse_lazy("noticia-list")

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super(NoticiaCreate, self).form_valid(form)


class ComentarioCreate(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = NuevoComentario
    template_name = "noticias/formulario_comentario.html"
    success_url = reverse_lazy("noticia-list")

    def get_context_data(self, **kwargs):
        context = super(ComentarioCreate, self).get_context_data(**kwargs)
        context['noticia'] = get_object_or_404(Noticia, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.noticia = get_object_or_404(Noticia, pk=self.kwargs['pk'])
        return super(ComentarioCreate, self).form_valid(form)


class FiltroNoticias(generic.ListView):
    model = Noticia
    template_name = "noticias/noticia_list.html"

    def get_queryset(self, *args, **kwargs):
        categoria = self.kwargs["pk"]
        return Noticia.objects.filter(categoria=categoria)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fecha'] = FormularioFecha
        return context


class CategoriaListView(generic.ListView):
    model = Categoria
    template_name = "noticias/lista_categorias.html"


class NoticiaDelete(LoginRequiredMixin, DeleteView):
    model = Noticia
    template_name = "noticias/borrado_noticia.html"
    success_url = reverse_lazy("noticia-list")

    def get_queryset(self):
        autor = self.request.user
        return self.model.objects.filter(autor=autor)


class ComentarioDelete(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = "noticias/borrado_comentario.html"
    success_url = reverse_lazy("noticia-list")

    def get_queryset(self):
        autor = self.request.user
        return self.model.objects.filter(autor=autor)


class NoticiaUpdate(LoginRequiredMixin, UpdateView):
    model = Noticia
    template_name = "noticias/editar_noticia.html"
    fields = ["titulo", "categoria", "imagen", "texto"]
    success_url = reverse_lazy("noticia-list")

    def get_queryset(self):
        autor = self.request.user
        return self.model.objects.filter(autor=autor)

class ComentarioUpdate(LoginRequiredMixin, UpdateView):
    model = Comentario
    template_name = "noticias/editar_comentario.html"
    fields = ["texto", ]
    success_url = reverse_lazy("noticia-list")

    def get_queryset(self):
        autor = self.request.user
        return self.model.objects.filter(autor=autor)


class BusquedaNoticia(FilterView):
    filterset_class = FiltroBusqueda
    template_name = 'noticias/busqueda.html'
