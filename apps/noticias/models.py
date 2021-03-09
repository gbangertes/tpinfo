from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Noticia(models.Model):
    autor = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='noticias')
    texto = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-created_date']

    # def publicar(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def get_absolute_url(self):
        return reverse('noticia-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.titulo
