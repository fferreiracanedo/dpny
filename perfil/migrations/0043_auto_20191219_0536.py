# Generated by Django 2.1.1 on 2019-12-19 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0042_auto_20191125_1018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfil',
            options={'ordering': ['nome'], 'verbose_name': 'Perfil', 'verbose_name_plural': 'Perfis'},
        ),
        migrations.AddField(
            model_name='perfil',
            name='visualizar_linkedin',
            field=models.BooleanField(default=False, verbose_name='Disponibilizar no Linkedin?'),
        ),
    ]
