# Generated by Django 2.1.1 on 2019-01-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0018_auto_20181106_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='proposito',
            field=models.TextField(blank=True, verbose_name='Propósito'),
        ),
    ]
