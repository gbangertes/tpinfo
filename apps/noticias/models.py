from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Noticia(models.Model):
    autor = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    categoria = models.ForeignKey('noticias.Categoria', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='noticias')
    texto = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']

    def get_absolute_url(self):
        return reverse('noticia-detail', args=[str(self.id)])

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    nombre = models.TextField(max_length=150)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('filtro-categoria', args=[str(self.id)])
