# Generated by Django 2.1.1 on 2019-11-13 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiencia_profissional', '0016_auto_20191106_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='requisitos_tecnicos',
            field=models.ManyToManyField(blank=True, to='pessoa.RequisitoTecnico', verbose_name='Requisitos Técnicos'),
        ),
    ]