from django.urls import path
from .views import (
    OrdemServicoListaView,
    OrdemServicoCriarView,
    OrdemServicoEditarView,
    OrdemServicoDeletarView
)

urlpatterns = [
    path('', OrdemServicoListaView.as_view(), name='ordemServicoLista'),
    path('novo/', OrdemServicoCriarView.as_view(), name='ordemServicoCriar'),
    path('<int:pk>/editar/', OrdemServicoEditarView.as_view(), name='ordemServicoEditar'),
    path('<int:pk>/deletar/', OrdemServicoDeletarView.as_view(), name='ordemServicoDeletar'),
]
