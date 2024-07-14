# Generated by Django 2.1.1 on 2018-10-16 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teste_psicologico', '0002_auto_20181016_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afirmativa',
            name='resposta_esperada',
            field=models.CharField(choices=[('CT', 'Concordo Totalmente'), ('C', 'Concordo'), ('I', 'Indiferente'), ('D', 'Discordo'), ('I', 'Discordo Totalmente')], max_length=3, verbose_name='Resposta Esperada'),
        ),
        migrations.AlterField(
            model_name='resposta',
            name='resposta_esperada',
            field=models.CharField(choices=[('CT', 'Concordo Totalmente'), ('C', 'Concordo'), ('I', 'Indiferente'), ('D', 'Discordo'), ('I', 'Discordo Totalmente')], max_length=3, verbose_name='Resposta Esperada'),
        ),
    ]
