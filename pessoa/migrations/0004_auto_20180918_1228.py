# Generated by Django 2.1 on 2018-09-18 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0003_auto_20180918_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='comunicacao',
            field=models.BooleanField(help_text='Desenvoltura, Coerencia entre discurso e acao, objetividade, capacidade de transmitir ideias e escutar. Capacidade de se comunicar com diferentes tipos de pessoas.', null=True, verbose_name='Comunicação'),
        ),
    ]