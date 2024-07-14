# Generated by Django 2.1.1 on 2019-11-06 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0060_auto_20191106_1124'),
        ('experiencia_profissional', '0014_cargo_superior'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cargo',
            options={'ordering': ['titulo']},
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='accontability',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='aprendizado_desenvolvimento',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='atendimento_cliente',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='atribuicoes',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='competitividade',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='comportamento',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='comunicacao',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='criatividade',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='equilibrio_emocional',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='etica',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='excelencia_operacional',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='gestao_mudanca',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='gestao_negocio',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='gestao_pessoas',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='inovacao',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='negociacao',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='protagonismo',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='relacionamento_interpessoal',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='solucao_problemas',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='superior',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='tomada_decisao',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='trabalho_equipe',
        ),
        migrations.AddField(
            model_name='cargo',
            name='atividades',
            field=models.TextField(blank=True, null=True, verbose_name='Atividades'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='codigo',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Código'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='missao',
            field=models.TextField(blank=True, null=True, verbose_name='Missão'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='requisitos_tecnicos',
            field=models.ManyToManyField(blank=True, null=True, to='pessoa.RequisitoTecnico', verbose_name='Requisitos Técnicos'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='responsabilidades',
            field=models.TextField(blank=True, null=True, verbose_name='Responsabilidades'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='titulo',
            field=models.CharField(default='Teste', max_length=150, verbose_name='Título'),
            preserve_default=False,
        ),
    ]
