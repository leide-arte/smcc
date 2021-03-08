from django.urls import path
from .views import DisciplinasListView, DisciplinasCreateView, DisciplinasEditarView, DisciplinasExcluirView

urlpatterns = [
        path('listar/', DisciplinasListView.as_view(), name= 'disciplinas_listar'),
        path('adicionar/', DisciplinasCreateView.as_view(), name= 'disciplinas_adicionar'),
        path('editar/<int:pk>', DisciplinasEditarView.as_view(), name='disciplinas_editar'),
        path('excluir/<int:pk>', DisciplinasExcluirView.as_view(), name='disciplinas_excluir'),

] 
