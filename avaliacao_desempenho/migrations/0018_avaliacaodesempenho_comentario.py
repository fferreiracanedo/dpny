# Generated by Django 2.2.4 on 2020-02-04 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao_desempenho', '0017_grupoavaliacaodesempenho_ja_gerado'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacaodesempenho',
            name='comentario',
            field=models.TextField(blank=True, null=True, verbose_name='Comentários'),
        ),
    ]