from django.db import models


class Aluno(models.Model):
    
    
    id=models.AutoField(primary_key=True, verbose_name='Cod.')
    alun_nome= models.CharField(default='', blank=False, null=False, max_length=150, verbose_name='Nome Completo', db_column='alun_nome')
    alun_email= models.EmailField(default='', blank=True, null=True, verbose_name='Email', db_column='alun_email')
    alun_telefone= models.CharField(default='', blank= True, null= True, max_length=12, verbose_name='Telefone',  db_column='alun_telefone')
    alun_cpf=models.CharField(default='',blank=True, null=True, max_length=12, verbose_name='cpf ', db_column='cpf')
    #alun_endereco=models.CharField(default='',   blank=True, null=True, max_length=150, verbose_name='Endereço', db_column='alun-endereço')
    #alun_bairro=models.CharField(default='',blank=True, null=True, max_length=150, verbose_name='Bairro', db_column='alun_bairro')
    alun_cidade=models.CharField(default='',blank=True, null=True, max_length=150, verbose_name='Cidade', db_column='alun_cidade')

    alun_fk_disc= models.ForeignKey('disciplinas.Disciplinas', default='', related_name='aluno_rel_disc', on_delete=models.DO_NOTHING, blank=True, null=True, db_column='alun_fk_disc', verbose_name='Disciplinas')

    ##alun_estado=models.CharField(default='',blank=True, null=True, max_length=150, verbose_name='Estado', db_column='alun_estado')
    #alun_datetime_inclusao=models.DateTimeField(max_length=50, blank= True, null=True, auto_now_add=True, verbose_name='Data/Hora Inclusão')
    #alun_datetime_alteracao=models.DateTimeField(max_length=50, blank=True, null=True, auto_now=True, verbose_name='Data/Hora Alteração')
   

class Meta:
    db_table='aluno'