# Generated by Django 3.1.7 on 2021-02-27 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='alun_whatsapp',
        ),
        migrations.AddField(
            model_name='aluno',
            name='alun_cpf',
            field=models.CharField(blank=True, db_column='cpf', default='', max_length=12, null=True, verbose_name='cpf '),
        ),
    ]
