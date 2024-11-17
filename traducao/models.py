from django.db import models

class Imagem(models.Model):
    imagem = models.ImageField(upload_to='imagens/')
    extraido = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Imagem {self.id}"