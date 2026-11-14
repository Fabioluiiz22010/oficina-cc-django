from django import forms
from django.forms import inlineformset_factory
from .models import OrdemServico, PecaUsada

class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        fields = [
            'veiculo',
            'servico',
            'quilometragemAtual',
            'dataSaida',
            'estaConcluida',
            'valorTotal'
        ]

PecaUsadaFormset = inlineformset_factory(
    OrdemServico,
    PecaUsada,
    fields=['peca', 'quantidadeUsada'],
    extra=1,
    can_delete=True
)
