# veiculos/urls.py
from django.urls import path
from .views import (
    VeiculoListaView, 
    VeiculoCriarView, 
    VeiculoEditarView, 
    VeiculoDeletarView
)

urlpatterns = [
    path('', VeiculoListaView.as_view(), name='veiculoLista'),
    path('novo/', VeiculoCriarView.as_view(), name='veiculoCriar'),
    path('<str:pk>/editar/', VeiculoEditarView.as_view(), name='veiculoEditar'),
    path('<str:pk>/deletar/', VeiculoDeletarView.as_view(), name='veiculoDeletar'),
]