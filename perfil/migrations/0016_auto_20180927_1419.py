# Generated by Django 2.1 on 2018-09-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0015_perfil_cargo'),
    ]

    operations = [
        migrations.AddField(
            model_name='analisetalento',
            name='visivel_site',
            field=models.BooleanField(default=False, help_text='Habilitar para que a análise seja exibida no site?', verbose_name='Análise visível no site?'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='visivel_site',
            field=models.BooleanField(default=False, help_text='Habilitar para que o perfil seja exibido no site?', verbose_name='Perfil visível no site?'),
        ),
    ]
