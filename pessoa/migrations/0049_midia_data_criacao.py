# Generated by Django 2.1.1 on 2019-10-29 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0048_auto_20191029_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='midia',
            name='data_criacao',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de Criação'),
        ),
    ]
