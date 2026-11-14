

from django.db import models

class Cliente(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True)  # CPF como chave primária
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nome} ({self.cpf})"
