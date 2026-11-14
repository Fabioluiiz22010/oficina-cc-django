# clientes/filters.py
import django_filters
from .models import Cliente

class ClienteFiltro(django_filters.FilterSet):
    # filtro por nome
    nomeCompleto = django_filters.CharFilter(
        field_name='nome', # nome do campo no Model
        lookup_expr='icontains', # pesquisa que não diferencia maiúsculas de minúsculas
        label='Buscar Cliente por Nome' 
    )
    
    # filtro por CPF
    cpfDoCliente = django_filters.CharFilter(
        field_name='cpf', # cpf
        lookup_expr='exact', # pesquisa exata
        label='Buscar por CPF'
    )

    