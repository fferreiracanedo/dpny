# Generated by Django 2.1.1 on 2019-12-19 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0045_perfil_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='data_abertura',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Abertura'),
        ),
    ]
