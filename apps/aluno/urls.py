from django.urls import path
from .views import AlunoListarView, AlunoAdicionarView, AlunoEditarView, AlunoExcluirView

urlpatterns=[
    path('listar/', AlunoListarView.as_view(), name='aluno_listar'),
    path('adicionar/',AlunoAdicionarView.as_view(), name='aluno_adicionar'),
    path('editar/<int:pk>',AlunoEditarView.as_view(), name='aluno_editar'),
    path('excluir/<int:pk>',AlunoExcluirView.as_view(), name='aluno_excluir'),
]
