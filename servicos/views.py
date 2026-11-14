from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Servico
from .filters import ServicoFiltro
 
class ServicoListaView(FilterView):  
    model = Servico
    filterset_class = ServicoFiltro
    template_name = 'servicos/servicoLista.html'
    context_object_name = 'servicos'
    paginate_by = 10

class ServicoCriarView(CreateView):
    model = Servico
    template_name = 'servicos/servicoCriarEditar.html'
    fields = ['nomeDoServico', 'descricaoDoServico', 'valorPadrao', 'ativo']
    success_url = reverse_lazy('servicoLista')


class ServicoEditarView(UpdateView):
    model = Servico
    template_name = 'servicos/servicoCriarEditar.html'
    fields = ['nomeDoServico', 'descricaoDoServico', 'valorPadrao', 'ativo']
    success_url = reverse_lazy('servicoLista')
    context_object_name = 'servico'

class ServicoDeletarView(DeleteView):
    model = Servico
    template_name = 'servicos/servicoConfirmarDelete.html'
    success_url = reverse_lazy('servicoLista')