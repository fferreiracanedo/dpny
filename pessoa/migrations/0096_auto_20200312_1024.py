# Generated by Django 2.2.4 on 2020-03-12 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0095_auto_20200312_1021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pessoa',
            options={'ordering': ['id'], 'verbose_name': 'Pessoa', 'verbose_name_plural': 'Pessoas'},
        ),
    ]