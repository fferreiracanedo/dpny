# Generated by Django 2.1.1 on 2019-12-09 13:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0063_experienciaprofissional_trabalho_atual'),
        ('configuracao_avaliacao_desempenho', '0003_potencial_explicativo'),
        ('avaliacao_desempenho', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoAvaliacaoDesempenho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('formato_avaliacao', models.CharField(choices=[('90', '90 graus'), ('180', '180 graus'), ('360', '360 graus')], default='90', max_length=3, verbose_name='Formato de Avaliação')),
                ('data_inicial', models.DateField(verbose_name='Data Inicial')),
                ('data_final', models.DateField(verbose_name='Data Final')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('data_criacao', models.DateTimeField(default=datetime.datetime.now, verbose_name='Data de Criação')),
                ('competencia', models.ManyToManyField(blank=True, null=True, to='configuracao_avaliacao_desempenho.Competencia', verbose_name='Competências')),
                ('pessoa', models.ManyToManyField(to='pessoa.Pessoa', verbose_name='Pessoa')),
                ('potencial', models.ManyToManyField(blank=True, null=True, to='configuracao_avaliacao_desempenho.Potencial', verbose_name='Potencial')),
            ],
            options={
                'verbose_name': 'Grupo de Avaliação',
                'verbose_name_plural': 'Grupos de Avaliações',
            },
        ),
    ]