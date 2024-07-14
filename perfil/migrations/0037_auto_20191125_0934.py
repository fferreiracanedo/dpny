# Generated by Django 2.1.1 on 2019-11-25 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0036_perfil_nivel_escolaridade_exigido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='nota_maxima_formacao_academica',
            field=models.CharField(choices=[('1.0', 'Trancado/Não Possui'), ('3.0', 'Cursando'), ('5.0', 'Concluído')], max_length=250, verbose_name='Nota Máxima para Formação Acadêmica'),
        ),
    ]