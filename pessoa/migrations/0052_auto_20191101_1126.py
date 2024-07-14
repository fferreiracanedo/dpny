# Generated by Django 2.1.1 on 2019-11-01 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0051_auto_20191031_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='documento',
            new_name='cpf_anexo',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cor',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Cor'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='ctps_anexo',
            field=models.FileField(blank=True, upload_to='documentos/', verbose_name='CTPS Digitalizada'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='ctps_data_expedicao',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Expedição'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='ctps_numero',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='CTPS'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='ctps_serie',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Série'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='ctps_uf',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='UF'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='habilitacao_categoria',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Categoria'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='habilitacao_numero',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Número da Habilitação'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='municipio_nascimento',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Município de Nascimento'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='nacionalidade',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nacionalidade'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='nome_mae',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome da Mãe'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='nome_pai',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome do Pai'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='pis_anexo',
            field=models.FileField(blank=True, upload_to='documentos/', verbose_name='PIS Digitalizado'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='rg',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='RG'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='rg_anexo',
            field=models.FileField(blank=True, upload_to='documentos/', verbose_name='RG Digitalizado'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='rg_data_expedicao',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Expedição'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='rg_orgao_expedidor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='RG - Orgão Expedidor'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='titulo_eleitor',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Título de Eleitor'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='titulo_eleitor_anexo',
            field=models.FileField(blank=True, upload_to='documentos/', verbose_name='Título de Eleitor Digitalizado'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='titulo_eleitor_secao',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Seção'),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='titulo_eleitor_zona',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Zona'),
        ),
    ]
