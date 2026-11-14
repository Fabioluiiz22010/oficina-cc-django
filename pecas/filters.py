import django_filters
from django.db.models import Q
from .models import Peca

class PecaFiltro(django_filters.FilterSet):
    # filtro por nome ou código
    buscaGeral = django_filters.CharFilter(
        method='filter_buscaGeral',
        label='Buscar (Nome ou Código)'
    )
    # filtro de estoque baixo (exemplo)
    estoqueBaixo = django_filters.BooleanFilter(
        method='filter_estoqueBaixo',
        label='Estoque Baixo (< 10 unidades)?'
    )

    class Meta:
        model = Peca
        fields = ['buscaGeral', 'estoqueBaixo'] 
    def filter_buscaGeral(self, queryset, name, value):
        return queryset.filter(
            Q(nomeDaPeca__icontains=value) | Q(codigoDaPeca__icontains=value)
        )
    def filter_estoqueBaixo(self, queryset, name, value):
        if value:
            return queryset.filter(quantidadeEmEstoque__lt=10)
        return queryset