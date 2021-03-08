from apps.disciplinas.models import Disciplinas
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView) 
from django.views.generic import (TemplateView, ListView, CreateView, UpdateView,DeleteView)
#, ListView, CreateView, UpdateView, DeleteView


class DisciplinasCreateView(CreateView):
    fields = ['disc_nome']
    model = Disciplinas
    template_name = 'disciplinas/disc_form.html'
    success_url = reverse_lazy('disciplinas_adicionar')

class DisciplinasListView(ListView):
    model= Disciplinas
    template_name = 'disciplinas/disc_listar.html'

class DisciplinasEditarView(UpdateView):
    model= Disciplinas 
    fields=[ 'disc_nome']
    template_name='disciplinas/disc_form.html'
    success_url= reverse_lazy('disciplinas_listar')
    
class DisciplinasExcluirView(DeleteView):
    model=Disciplinas
    template_name='disciplinas/disc_deletar.html'
    fields=['disc_nome']
    success_url= reverse_lazy('disciplinas_listar')

    
    
   

