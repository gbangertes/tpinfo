from django import forms
from .models import Noticia
from apps.comentarios.models import Comentario
from django.forms.widgets import SelectDateWidget


class NuevaNoticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ["titulo", "categoria", "imagen", "texto"]


class NuevoComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["texto", ]


class FormularioFecha(forms.Form):
    fecha = forms.DateField(widget=SelectDateWidget())
