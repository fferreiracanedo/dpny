# Generated by Django 2.1 on 2018-09-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_auto_20180919_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analisetalento',
            name='nota_essencia_talento',
            field=models.CharField(max_length=30, verbose_name='Essência/Talento'),
        ),
    ]
