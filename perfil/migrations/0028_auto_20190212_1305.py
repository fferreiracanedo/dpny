# Generated by Django 2.1.1 on 2019-02-12 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0027_auto_20190212_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analisetalento',
            name='disponivel_projeto',
            field=models.BooleanField(default=True, verbose_name='Disponível para o projeto?'),
        ),
    ]