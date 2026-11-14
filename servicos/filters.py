import django_filters
from .models import Servico

class ServicoFiltro(django_filters.FilterSet):
    # filtro por nome do serviço
    nomeDoServico = django_filters.CharFilter(
        field_name='nomeDoServico', 
        lookup_expr='icontains',
        label='Buscar Serviço'
    )
    # filtro por status
    ativo = django_filters.BooleanFilter(
        field_name='ativo',
        label='Status Ativo'
    )

    class Meta:
        model = Servico
        fields = ['nomeDoServico', 'ativo']