from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.forms.models import inlineformset_factory
from django_filters.views import FilterView

from .models import OrdemServico, PecaUsada
from .filters import OrdemServicoFiltro


PecaUsadaFormset = inlineformset_factory(
    OrdemServico,
    PecaUsada,
    fields=('peca', 'quantidadeUsada'),
    extra=1,
    can_delete=True
)


class OrdemServicoListaView(FilterView):
    model = OrdemServico
    filterset_class = OrdemServicoFiltro
    template_name = 'ordemServicos/ordemServicoLista.html'
    context_object_name = 'ordensServico'
    paginate_by = 10

class OrdemServicoCriarView(CreateView):
    model = OrdemServico
    template_name = 'ordemServicos/ordemServicoCriarEditar.html'
    fields = ['veiculo', 'servico', 'quilometragemAtual', 'valorTotal']
    success_url = reverse_lazy('ordemServicoLista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['pecasFormset'] = PecaUsadaFormset(self.request.POST)
        else:
            context['pecasFormset'] = PecaUsadaFormset()
        context['ordemServico'] = None
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        pecasFormset = PecaUsadaFormset(request.POST)
        if form.is_valid() and pecasFormset.is_valid():
            return self.form_valid(form, pecasFormset)
        return self.form_invalid(form, pecasFormset)

    def form_valid(self, form, pecasFormset):
        self.object = form.save()
        pecasFormset.instance = self.object
        pecasFormset.save()
        return redirect(self.success_url)

    def form_invalid(self, form, pecasFormset):
        return self.render_to_response(self.get_context_data(form=form, pecasFormset=pecasFormset))

class OrdemServicoEditarView(UpdateView):
    model = OrdemServico
    template_name = 'ordemServicos/ordemServicoCriarEditar.html'
    fields = ['veiculo', 'servico', 'quilometragemAtual', 'valorTotal']
    success_url = reverse_lazy('ordemServicoLista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['pecasFormset'] = PecaUsadaFormset(self.request.POST, instance=self.object)
        else:
            context['pecasFormset'] = PecaUsadaFormset(instance=self.object)
        context['ordemServico'] = self.object
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        pecasFormset = PecaUsadaFormset(request.POST, instance=self.object)
        if form.is_valid() and pecasFormset.is_valid():
            return self.form_valid(form, pecasFormset)
        return self.form_invalid(form, pecasFormset)

    def form_valid(self, form, pecasFormset):
        self.object = form.save()
        pecasFormset.save()
        return redirect(self.success_url)

    def form_invalid(self, form, pecasFormset):
        return self.render_to_response(self.get_context_data(form=form, pecasFormset=pecasFormset))


class OrdemServicoDeletarView(DeleteView):
    model = OrdemServico
    template_name = 'ordemServicos/ordemServicoConfirmarDelete.html'
    success_url = reverse_lazy('ordemServicoLista')
