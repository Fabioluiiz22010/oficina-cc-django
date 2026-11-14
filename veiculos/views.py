from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from .models import Veiculo
from clientes.models import Cliente
from ordemServicos.models import OrdemServico
from pecas.models import Peca
from servicos.models import Servico
from .filters import VeiculoFiltro

class VeiculoListaView(FilterView):
    model = Veiculo
    filterset_class = VeiculoFiltro
    template_name = 'veiculos/veiculoLista.html'
    context_object_name = 'veiculos'
    paginate_by = 10

class VeiculoCriarView(CreateView):
    model = Veiculo
    template_name = 'veiculos/veiculoCriarEditar.html'
    fields = ['placaDoVeiculo', 'marcaDoVeiculo', 'modeloDoVeiculo', 'anoDeFabricacao', 'corDoVeiculo', 'proprietarioDoVeiculo']
    success_url = reverse_lazy('veiculoLista')


class VeiculoEditarView(UpdateView):
    model = Veiculo
    template_name = 'veiculos/veiculoCriarEditar.html'
    fields = ['placaDoVeiculo', 'marcaDoVeiculo', 'modeloDoVeiculo', 'anoDeFabricacao', 'corDoVeiculo', 'proprietarioDoVeiculo']
    success_url = reverse_lazy('veiculoLista')
    context_object_name = 'veiculo'



class VeiculoDeletarView(DeleteView):
    model = Veiculo
    template_name = 'veiculos/veiculoConfirmarDelete.html'
    success_url = reverse_lazy('veiculoLista')