from django.db import models

class Categorias(models.model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
