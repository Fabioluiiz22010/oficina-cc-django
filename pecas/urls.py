from django.urls import path
from .views import (
    PecaListaView, 
    PecaCriarView, 
    PecaEditarView, 
    PecaDeletarView
)

urlpatterns = [ 
    path('', PecaListaView.as_view(), name='pecaLista'),
    path('novo/', PecaCriarView.as_view(), name='pecaCriar'),
    path('<str:pk>/editar/', PecaEditarView.as_view(), name='pecaEditar'),
    path('<str:pk>/deletar/', PecaDeletarView.as_view(), name='pecaDeletar'),
]