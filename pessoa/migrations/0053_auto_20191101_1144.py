# Generated by Django 2.1.1 on 2019-11-01 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0052_auto_20191101_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='rg_orgao_expedidor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Orgão Expedidor'),
        ),
    ]