from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Peca
from .filters import PecaFiltro

 
class PecaListaView(FilterView):   
    model = Peca
    filterset_class = PecaFiltro
    template_name = 'pecas/pecaLista.html'
    context_object_name = 'pecas'
    paginate_by = 10
 
class PecaCriarView(CreateView):  
    model = Peca
    template_name = 'pecas/pecaCriarEditar.html' 
    fields = ['nomeDaPeca', 'codigoDaPeca', 'quantidadeEmEstoque', 'precoDeVenda']
    success_url = reverse_lazy('pecaLista')
 
class PecaEditarView(UpdateView): 
    model = Peca
    template_name = 'pecas/pecaCriarEditar.html'
 
    fields = ['nomeDaPeca', 'codigoDaPeca', 'quantidadeEmEstoque', 'precoDeVenda']
    success_url = reverse_lazy('pecaLista')
    context_object_name = 'peca'
 
class PecaDeletarView(DeleteView):  
    model = Peca
    template_name = 'pecas/pecaConfirmarDelete.html'
    success_url = reverse_lazy('pecaLista')