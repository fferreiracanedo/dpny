# Generated by Django 2.2.4 on 2020-02-07 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuracao_avaliacao_desempenho', '0009_competencia_ordem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='competencia',
            options={'ordering': ['ordem'], 'verbose_name': 'Competência', 'verbose_name_plural': 'Competências'},
        ),
    ]