from django import forms
from .models import Noticia
from apps.comentarios.models import Comentario

class NuevaNoticia(forms.ModelForm):
	class Meta:
		model = Noticia
		fields = ["titulo", "imagen", "texto"]

class NuevoComentario(forms.ModelForm):
	class Meta:
		model = Comentario
		fields = ["texto",  ]
