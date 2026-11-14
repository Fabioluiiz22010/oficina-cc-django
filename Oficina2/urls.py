# Seu projeto principal / urls.py

from django.contrib import admin
from django.urls import path, include
# 🎯 IMPORTAÇÃO NECESSÁRIA
from clientes.views import HomeDashboardView 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 🎯 CORREÇÃO CRUCIAL: Mapeamento direto da Home/Dashboard para a raiz (/)
    # Isso resolve o 404 e garante que o seu app 'clientes' possa ser incluído abaixo.
    path('', HomeDashboardView.as_view(), name='home'), 
    
    # Mapeamento dos apps com prefixo de URL
    # É uma boa prática incluir o próprio app de clientes aqui para acessar
    # os demais caminhos (lista, criar, editar) através de /clientes/
    path('clientes/', include('clientes.urls')),
    path('ordemServicos/', include('ordemServicos.urls')),
    path('servicos/', include('servicos.urls')),
    path('veiculos/', include('veiculos.urls')),
    path('pecas/', include('pecas.urls')),
]