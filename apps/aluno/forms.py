from django.forms import ModelForm, fields
from django import forms
from .models import Aluno 
from apps.disciplinas.models import Disciplinas

class AlunoForm(ModelForm):
    alun_nome= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control m-3'}), label='Nome:')
    alun_email= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control m-3'}), label='Email:')
    alun_telefone= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control m-3'}), label='Telefone:')
    alun_cpf= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control m-3'}), label='CPF:')
    alun_cidade= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control m-3'}), label='Cidade:')
    alun_fk_disc= forms.ModelChoiceField( widget= forms.Select(attrs={'class':'form-control m-3'}), queryset=Disciplinas.objects, label='Disciplinas')
    class Meta: 
        model= Aluno
        fields =['alun_nome', 'alun_email', 'alun_telefone', 'alun_cpf', 'alun_cidade',
        'alun_fk_disc']
       
