from django.db import models



class Disciplinas(models.Model):
    id=models.AutoField(primary_key=True, verbose_name='Cod.')
    disc_nome= models.CharField(default='', blank=False, null=False, max_length=150,  verbose_name='Nome da disciplina', db_column='disc_nome')

    
    class Meta:
        db_table='disciplinas'

    def __str__(self):
        return  self.disc_nome

