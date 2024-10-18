from django.db import models

class Atividades(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateField()

    def __str__(self):
        return self.nome


class Classes(models.Model):
    serie = models.CharField(max_length=255)
    tamanho = models.IntegerField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateField()

    def __str__(self):
        return self.serie  # Corrigido para 'serie'