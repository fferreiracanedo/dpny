# Generated by Django 2.1.1 on 2019-12-19 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0044_auto_20191219_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='status',
            field=models.CharField(choices=[('Aberta', 'Aberta'), ('Encerrada', 'Encerrada'), ('Cancelada', 'Cancelada')], default='Aberta', max_length=20, verbose_name='Status'),
        ),
    ]
