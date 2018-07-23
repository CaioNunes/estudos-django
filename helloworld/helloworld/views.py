from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from helloworld.models import Funcionario
# Create your views here.


class IndexTemplateView(TemplateView):
    template_name = "index.html"


class FuncionarioListView(ListView):
    template_name = 'website/lista.html'
    model = Funcionario
    context_object_name = "funcionarios"


class FuncionarioUpdateView(UpdateView):
    template_name = 'atualiza.html'
    model = Funcionario
    fields = '__all__'



class FuncionarioDeleteView(DeleteView):
    template_name = "website/exclui.html"
    model = Funcionario
    context_object_name = 'funcionario'
    success_url = reverse_lazy("website:lista_funcionarios")


class FuncionarioCreateView(CreateView):
    template_name = "website/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy(
        "website:lista_funcionarios"
    )