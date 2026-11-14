 
from django.db import models

class Peca(models.Model):
    nomeDaPeca = models.CharField(max_length=150, unique=False, null=True, blank=True)
    codigoDaPeca = models.CharField(max_length=50, unique=False, null=True, blank=True)  
    quantidadeEmEstoque = models.PositiveIntegerField(default=0) 
    precoDeVenda = models.DecimalField(max_digits=10, decimal_places=2)  
    
    def __str__(self):
        return f"{self.nomeDaPeca} ({self.codigoDaPeca})"