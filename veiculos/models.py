from django.db import models
from clientes.models import Cliente

class Veiculo(models.Model):
    placaDoVeiculo = models.CharField(max_length=10, unique=True)
    marcaDoVeiculo = models.CharField(max_length=50)
    modeloDoVeiculo = models.CharField(max_length=50)
    anoDeFabricacao = models.IntegerField()
    corDoVeiculo = models.CharField(max_length=30)
    proprietarioDoVeiculo = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marcaDoVeiculo} {self.modeloDoVeiculo} ({self.placaDoVeiculo})"