import django_filters
from .models import OrdemServico

class OrdemServicoFiltro(django_filters.FilterSet):
# filtro por placa do veículo
    placa = django_filters.CharFilter(
        field_name='veiculo__placaDoVeiculo',
        lookup_expr='icontains',
        label='Placa'
    )
    # filtro por status
    estaConcluida = django_filters.BooleanFilter(
        field_name='estaConcluida',
        label='Concluída?'
    )

    class Meta:
        model = OrdemServico
        fields = ['placa', 'estaConcluida']
