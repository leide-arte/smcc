from apps.aluno.models import Aluno
from django.shortcuts import render
from  django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, CreateView, UpdateView,DeleteView)
from .forms import AlunoForm
from django.contrib.auth.mixins import LoginRequiredMixin

#from django.views.generic.base import TemplateView
#from django views.generic.list import AlunoListarView
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
class AlunoAdicionarView( LoginRequiredMixin, CreateView):
    model= Aluno 
    template_name='aluno/aluno_form.html'
    success_url= reverse_lazy('aluno_listar')
    form_class=AlunoForm
    #fields= [ 'alun_nome','alun_email', 'alun_telefone', 'alun_cpf', 'alun_cidade',  ]

class AlunoListarView( LoginRequiredMixin, ListView):
    model= Aluno
    template_name='aluno/listar.html'

class AlunoEditarView( LoginRequiredMixin, UpdateView):
    model= Aluno
    template_name='aluno/aluno_form.html'
    form_class=AlunoForm
    #fields= [ 'alun_nome','alun_email', 'alun_telefone', 'alun_cpf', 'alun_cidade']
    success_url= reverse_lazy('aluno_listar')
class AlunoExcluirView( LoginRequiredMixin, DeleteView):
    model= Aluno
    template_name='aluno/excluir.html'
    fields= [ 'alun_nome','alun_email', 'alun_telefone', 'alun_cpf', 'alun_cidade', 'alun_fk_disc']
    success_url= reverse_lazy('aluno_listar')
