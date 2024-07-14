# Generated by Django 2.1.1 on 2019-10-09 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20191009_1002'),
        ('pessoa', '0030_auto_20191009_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='estado_civil',
            field=models.ForeignKey(help_text='Campo Obrigatório*', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.EstadoCivil', verbose_name='Estado Civil'),
        ),
    ]
