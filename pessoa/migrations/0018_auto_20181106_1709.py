# Generated by Django 2.1.1 on 2018-11-06 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0017_auto_20181106_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='instituicao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formacao.Instituicao', verbose_name='Instituição'),
        ),
        migrations.AlterField(
            model_name='especializacao',
            name='instituicao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formacao.Instituicao', verbose_name='Instituição'),
        ),
        migrations.AlterField(
            model_name='formacaoacademica',
            name='instituicao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formacao.Instituicao', verbose_name='Instituição'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
