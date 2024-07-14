# Generated by Django 2.1.1 on 2018-10-10 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiencia_profissional', '0011_cargo_area_atuacao'),
        ('formacao', '0008_auto_20181010_0841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='especializacao',
            name='area_atuacao',
        ),
        migrations.RemoveField(
            model_name='formacaoacademica',
            name='area_atuacao',
        ),
        migrations.AddField(
            model_name='curso',
            name='area_atuacao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='experiencia_profissional.AreaAtuacao', verbose_name='Área de Atuação'),
            preserve_default=False,
        ),
    ]