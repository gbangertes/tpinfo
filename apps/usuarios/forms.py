from django.contrib.auth import forms
from .models import Usuario

class Formulario_Alta_Usuario(forms.UserCreationForm):
	class Meta:
		model = Usuario
		fields = ["username","first_name","last_name","email","password1","password2"]

