# Generated by Django 2.2.4 on 2020-01-29 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0084_auto_20200129_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='experienciaprofissional',
            name='cargo_atual',
            field=models.BooleanField(default=False, verbose_name='Cargo Atual'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='habilitacao_anexo',
            field=models.FileField(blank=True, upload_to='documentos/', verbose_name='Habilitação Digitalizada'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='residencia_anexo',
            field=models.FileField(blank=True, upload_to='documentos/', verbose_name='Comprovante de Residência Digitalizado'),
        ),
    ]
