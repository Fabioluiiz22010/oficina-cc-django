from django.urls import path
from .views import (
    ServicoListaView, 
    ServicoCriarView, 
    ServicoEditarView, 
    ServicoDeletarView
)

urlpatterns = [ 
    path('', ServicoListaView.as_view(), name='servicoLista'),  
    path('novo/', ServicoCriarView.as_view(), name='servicoCriar'), 
    path('<str:pk>/editar/', ServicoEditarView.as_view(), name='servicoEditar'), 
    path('<str:pk>/deletar/', ServicoDeletarView.as_view(), name='servicoDeletar'),
]