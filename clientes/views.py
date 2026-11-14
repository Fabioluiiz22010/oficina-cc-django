from django.shortcuts import render, redirect, get_object_or_404
from veiculos.models import Veiculo
from .models import Cliente
from ordemServicos.models import OrdemServico
from pecas.models import Peca
from servicos.models import Servico
from .filters import ClienteFiltro 
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView
from django.views.generic import ListView
from django_filters.views import FilterView

class HomeDashboardView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ordensEmServico = OrdemServico.objects.filter(estaConcluida=False).order_by('-dataEntrada')[:5]
        ordensAbertasCount = OrdemServico.objects.filter(estaConcluida=False).count()
        context['ordensAbertasCount'] = ordensAbertasCount
        context['ordensEmServico'] = ordensEmServico

        return context
class VeiculoBuscarView(ListView):
    model = Veiculo
    template_name = 'clientes/lista.html'
    context_object_name = 'veiculos'
    def get_queryset(self):
        placa = self.request.GET.get('placa')
        if placa:
            queryset = Veiculo.objects.filter(placaDoVeiculo__icontains=placa)
            # Se não houver placa, retorna um nada
            queryset = Veiculo.objects.none()
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['veiculosEmServicos'] = Veiculo.objects.none() 
        return context
    
class ClienteListaView(FilterView):
    model = Cliente
    template_name = 'clientes/listaClientes.html'
    context_object_name = 'clientes'
    paginate_by = 10 #quantidade de itens por página
    filterset_class = ClienteFiltro

class ClienteCriarView(CreateView):
    model = Cliente
    template_name = 'clientes/criarCliente.html'
    fields = ['nome', 'cpf', 'email']
    success_url = reverse_lazy('clienteLista')

class ClienteEditarView(UpdateView):
    model = Cliente
    template_name = 'clientes/criarCliente.html'
    fields = ['nome', 'email', 'cpf']
    success_url = reverse_lazy('clienteLista')
    context_object_name = 'cliente'

class ClienteDeletarView(DeleteView):
    model = Cliente
    template_name = 'clientes/clienteConfirmarDelete.html' 
    success_url = reverse_lazy('clienteLista')