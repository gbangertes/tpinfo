from django.db import models
from django.utils import timezone

# Create your models here.

class Comentario(models.Model):
    autor = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    noticia = models.ForeignKey('noticias.Noticia', on_delete=models.CASCADE)
    texto = models.TextField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.texto
