from django.shortcuts import render
from django.views import generic
from .models import Noticia 
from apps.comentarios.models import  Comentario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from .forms import NuevaNoticia


# Create your views here.

# def recientes(request):
#     recientes = Noticia.objects.all().reverse()[:10]
#     ctx = {}
#     ctx["noticias"] = recientes
#     return render(request, "recientes.html", ctx)

class NoticiaDetailView(generic.DetailView):
    model = Noticia

class NoticiaListView(generic.ListView):
    model = Noticia
    paginate_by = 10

class NoticiaCreate(LoginRequiredMixin, CreateView):
    model = Noticia
    form_class = NuevaNoticia
    template_name = "noticias/nueva_noticia.html"
    success_url = reverse_lazy("noticia-list")

class ComentarioCreate(LoginRequiredMixin, CreateView):
    model = Comentario
    fields = ['texto', ]
    
    def get_context_data(self, **kwargs):
        context = super(ComentarioCreate, self).get_context_data(**kwargs)
        context['noticia'] = get_object_or_404(Noticia, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.noticia = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return super(ComentarioCreate, self).form_valid(form)
