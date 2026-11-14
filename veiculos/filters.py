
import django_filters
from .models import Veiculo
from clientes.models import Cliente
class VeiculoFiltro(django_filters.FilterSet):
    placaDoVeiculo = django_filters.CharFilter(
        field_name='placaDoVeiculo', 
        lookup_expr='icontains',
        label='Buscar Placa'
    )
    marcaDoVeiculo = django_filters.CharFilter(
        field_name='marcaDoVeiculo', 
        lookup_expr='icontains',
        label='Buscar Marca'
    )
    proprietarioDoVeiculo = django_filters.ModelChoiceFilter(
        queryset=Cliente.objects.all(),
        label='Proprietário'
    )

    class Meta:
        model = Veiculo
        fields = ['placaDoVeiculo', 'marcaDoVeiculo', 'proprietarioDoVeiculo']