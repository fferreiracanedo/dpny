# Generated by Django 2.1.1 on 2019-12-19 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao_desempenho', '0013_avaliacaodesempenho_resposta_potencial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupoavaliacaodesempenho',
            name='formato_avaliacao',
        ),
        migrations.RemoveField(
            model_name='grupoavaliacaodesempenho',
            name='potencial',
        ),
    ]