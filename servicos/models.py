 
from django.db import models

class Servico(models.Model):
    nomeDoServico = models.CharField(max_length=100)  
    descricaoDoServico = models.TextField(blank=True) 
    valorPadrao = models.DecimalField(max_digits=10, decimal_places=2) 
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nomeDoServico