# Generated by Django 2.2.4 on 2020-03-12 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0094_pessoa_pares_avaliadores'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pessoa',
            options={'ordering': ['nome'], 'verbose_name': 'Pessoa', 'verbose_name_plural': 'Pessoas'},
        ),
    ]
