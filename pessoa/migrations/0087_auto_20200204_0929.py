# Generated by Django 2.2.4 on 2020-02-04 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0086_auto_20200130_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formacaoacademica',
            name='situacao',
            field=models.CharField(choices=[('Concluído', 'Concluído'), ('Cursando', 'Cursando'), ('Incompleto', 'Incompleto')], max_length=50, verbose_name='Situação'),
        ),
    ]