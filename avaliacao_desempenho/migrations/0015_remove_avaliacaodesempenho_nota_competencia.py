# Generated by Django 2.1.1 on 2020-01-02 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao_desempenho', '0014_auto_20191219_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacaodesempenho',
            name='nota_competencia',
        ),
    ]