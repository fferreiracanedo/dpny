# Generated by Django 2.1 on 2018-09-18 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formacao', '0004_auto_20180913_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='carga_horaria',
        ),
    ]