# Generated by Django 2.1.1 on 2019-11-07 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teste_psicologico', '0010_afirmativa_teste_psicologico'),
    ]

    operations = [
        migrations.AddField(
            model_name='testepsicologico',
            name='aprovado_gestor',
            field=models.BooleanField(default=False, verbose_name='Teste Aprovado'),
        ),
        migrations.AddField(
            model_name='testepsicologico',
            name='respondido',
            field=models.BooleanField(default=False, verbose_name='Teste Respondido'),
        ),
    ]
