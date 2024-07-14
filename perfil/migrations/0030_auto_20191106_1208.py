# Generated by Django 2.1.1 on 2019-11-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0029_auto_20191106_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='disponivel_pre_analise',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='nota_maxima_especializacao',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='nota_maxima_essencia_talento',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='nota_maxima_performance',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='projeto',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='visivel_site',
        ),
        migrations.AddField(
            model_name='perfil',
            name='nota_requisitos_tecnicos',
            field=models.CharField(choices=[('1.0', '1 Ponto'), ('2.0', '2 Pontos'), ('3.0', '3 Pontos'), ('4.0', '4 Pontos'), ('5.0', '5 Pontos')], default=1, max_length=250, verbose_name='Nota Máxima para Requisitos Técnicos'),
            preserve_default=False,
        ),
    ]