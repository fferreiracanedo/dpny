# Generated by Django 2.2.4 on 2020-03-02 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0046_perfil_data_abertura'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='visualizar_funcionarios',
            field=models.BooleanField(default=False, verbose_name='Disponibilizar para funcionários?'),
        ),
    ]
