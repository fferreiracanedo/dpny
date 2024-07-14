# Generated by Django 2.1 on 2018-09-18 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formacao', '0005_remove_curso_carga_horaria'),
        ('experiencia_profissional', '0004_auto_20180913_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetenciaProfissional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Competência Profissional',
                'verbose_name_plural': 'Competências Profissionais',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carga_horaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formacao.CargaHoraria', verbose_name='Carga Horária')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formacao.Curso', verbose_name='Curso')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formacao.Instituicao', verbose_name='Instituição')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Especializacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_formacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formacao.AnoFormacao', verbose_name='Ano de Formação')),
                ('especializacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formacao.Especializacao', verbose_name='Especialização')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formacao.Instituicao', verbose_name='Instituição')),
            ],
            options={
                'verbose_name': 'Especialização',
                'verbose_name_plural': 'Especializações',
            },
        ),
        migrations.CreateModel(
            name='ExperienciaProfissional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instituicao', models.CharField(max_length=150)),
                ('performance', models.CharField(blank=True, choices=[('1', 'Não atinge o esperado'), ('2', 'As vezes atinge'), ('3', 'Atinge'), ('4', 'As vezes supera'), ('5', 'Sempre supera')], max_length=1, verbose_name='Performance')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiencia_profissional.Cargo', verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Experiência Profissional',
                'verbose_name_plural': 'Experiências Profissionais',
            },
        ),
        migrations.CreateModel(
            name='FormacaoAcademica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_formacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formacao.AnoFormacao', verbose_name='Ano de Formação')),
                ('formacao_academica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formacao.FormacaoAcademica', verbose_name='Formação')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formacao.Instituicao', verbose_name='Instituição')),
            ],
            options={
                'verbose_name': 'Formação Acadêmica',
                'verbose_name_plural': 'Formações Acadêmicas',
            },
        ),
        migrations.CreateModel(
            name='HabilidadePessoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Habilidade Pessoal',
                'verbose_name_plural': 'Habilidades Pessoais',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome Completo')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('bairro', models.CharField(blank=True, max_length=150, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, max_length=150, verbose_name='Cidade')),
                ('telefone', models.CharField(blank=True, max_length=30, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('cargo_atual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiencia_profissional.Cargo', verbose_name='Cargo Atual')),
                ('competencia_profissional', models.ManyToManyField(to='pessoa.CompetenciaProfissional')),
                ('habilidade_pessoal', models.ManyToManyField(to='pessoa.HabilidadePessoal')),
                ('idioma', models.ManyToManyField(to='formacao.Idioma')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.AddField(
            model_name='formacaoacademica',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.Pessoa', verbose_name='Pessoa'),
        ),
        migrations.AddField(
            model_name='experienciaprofissional',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.Pessoa', verbose_name='Perfil'),
        ),
        migrations.AddField(
            model_name='experienciaprofissional',
            name='tempo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiencia_profissional.Experiencia', verbose_name='Tempo'),
        ),
        migrations.AddField(
            model_name='especializacao',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.Pessoa', verbose_name='Perfil'),
        ),
        migrations.AddField(
            model_name='curso',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.Pessoa', verbose_name='Pessoa'),
        ),
    ]