from django import forms
from .models import Noticia

class NuevaNoticia(forms.ModelForm):
	class Meta:
		model = Noticia
		fields = ["titulo", "imagen", "texto"]
