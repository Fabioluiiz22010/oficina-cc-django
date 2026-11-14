from django.urls import path
from .views import (
    ClienteListaView,
    ClienteCriarView,
    ClienteEditarView,
    ClienteDeletarView,
    HomeDashboardView,
    VeiculoBuscarView,
)

urlpatterns = [
    
    path('home/', HomeDashboardView.as_view(), name='homeDashboard'),
    path('', ClienteListaView.as_view(), name='clienteLista'),
    path('buscar_veiculo/', VeiculoBuscarView.as_view(), name='buscarVeiculo'),
    path('novo/', ClienteCriarView.as_view(), name='clienteCriar'),
    path('<str:pk>/editar/', ClienteEditarView.as_view(), name='clienteEditar'),
    path('<str:pk>/deletar/', ClienteDeletarView.as_view(), name='clienteDeletar'),
]