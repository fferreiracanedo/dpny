# Generated by Django 2.1.1 on 2019-02-12 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0023_auto_20190211_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='analisetalento',
            name='alocado',
            field=models.BooleanField(default=False, verbose_name='Alocado em projeto?'),
        ),
    ]
