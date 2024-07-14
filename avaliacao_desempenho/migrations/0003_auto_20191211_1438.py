# Generated by Django 2.1.1 on 2019-12-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao_desempenho', '0002_grupoavaliacaodesempenho'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcompetencia',
            name='nota',
            field=models.IntegerField(default=0, verbose_name='Nota'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itempotencial',
            name='nota',
            field=models.IntegerField(default=0, verbose_name='Nota'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grupoavaliacaodesempenho',
            name='formato_avaliacao',
            field=models.CharField(choices=[('AA', 'Auto Avaliação'), ('AG', 'Avaliação de Gestor'), ('AS', 'Avaliação de Subordinados'), ('AP', 'Avaliação de Pares')], default='90', max_length=3, verbose_name='Formato de Avaliação'),
        ),
    ]
