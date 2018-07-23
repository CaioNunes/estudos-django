#Importa a função index() definida no arquivo views.py
from django.urls import path
from helloworld.views import IndexTemplateView, FuncionarioListView, FuncionarioUpdateView, FuncionarioDeleteView, FuncionarioCreateView

app_name = 'website'

urlpatterns = [
    #GET
    path('', IndexTemplateView.as_view(), name='index'),

    path('funcionarios/', FuncionarioListView.as_view(), name='lista_funcionarios'),

    path('funcionario/<id>', FuncionarioUpdateView.as_view(), name="atualiza_funcionario"),

    path('funcionario/<id>', FuncionarioDeleteView.as_view(), name="deleta_funcionario"),

    path('funcionario/cadastrar', FuncionarioCreateView.as_view(), name="cadastra_funcionario")
]