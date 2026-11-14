# Oficina C&C — sistema de oficina mecânica em Django

Sistema web para uma oficina mecânica: cadastro de clientes, veículos, serviços, peças e ordens de serviço, com filtros e paginação em todas as listagens.

Projeto final da disciplina **Programação Avançada II** (Análise e Desenvolvimento de Sistemas, UniSALESIANO Araçatuba), entregue em novembro de 2025.

## Funcionalidades

- CRUD completo de clientes, veículos, serviços, peças e ordens de serviço
- Ordem de serviço ligada a um veículo e a um serviço, com as peças usadas e a quantidade de cada uma
- Controle de estoque e preço de venda das peças
- Filtros de busca em cada listagem (django-filter) e paginação de 10 itens
- Busca de veículo a partir da tela de clientes
- Painel inicial (home) e área administrativa do Django

## Stack

- Python e Django 5.2
- django-filter
- MySQL
- Class-based views (ListView, CreateView, UpdateView, DeleteView, FilterView)
- HTML e CSS com templates do Django

## Modelo de dados

| App | Modelo | Relações |
| --- | --- | --- |
| clientes | Cliente (CPF como chave primária) | — |
| veiculos | Veiculo | pertence a um Cliente |
| servicos | Servico | — |
| pecas | Peca | — |
| ordemServicos | OrdemServico | um Veiculo, um Servico e várias Pecas |
| ordemServicos | PecaUsada | tabela intermediária entre OrdemServico e Peca, com a quantidade usada |

## Como rodar

1. Crie um banco MySQL chamado `Oficina_C_e_C`.
2. Ajuste usuário e senha do banco em `Oficina2/settings.py` (o padrão do projeto é `root` / `root`).
3. Instale as dependências e rode as migrações:

```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install "django==5.2.*" django-filter mysqlclient
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

4. Acesse `http://127.0.0.1:8000/`.

## Estrutura

```
Oficina2/        configurações e rotas principais
clientes/        app de clientes (models, views, filtros, templates)
veiculos/        app de veículos
servicos/        app de serviços
pecas/           app de peças
ordemServicos/   app de ordens de serviço
templates/       layout base e home
static/          CSS e imagens
docs/            proposta inicial do projeto (PDF)
```

## Observações

- Projeto acadêmico. `DEBUG` está ligado e a `SECRET_KEY` e a senha do banco estão no `settings.py`; troque antes de usar fora do ambiente local.
- A mesma oficina aparece em outros dois repositórios: [oficina-api-flask](https://github.com/Fabioluiiz22010/oficina-api-flask) (API REST) e [mecanica-cc-jsf](https://github.com/Fabioluiiz22010/mecanica-cc-jsf) (Java com JSF).

## Autor

Fabio Luiz Florêncio da Silva · [github.com/Fabioluiiz22010](https://github.com/Fabioluiiz22010) · [LinkedIn](https://www.linkedin.com/in/fabio-l-florencio/)
