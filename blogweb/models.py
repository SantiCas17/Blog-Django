from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='posteos', null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor.username}"