# Generated by Django 2.1.1 on 2018-10-23 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0018_configanalisetalento'),
    ]

    operations = [
        migrations.AddField(
            model_name='configanalisetalento',
            name='quantidade_atual_analises',
            field=models.IntegerField(default=0, verbose_name='Número Atual de Análises'),
            preserve_default=False,
        ),
    ]
