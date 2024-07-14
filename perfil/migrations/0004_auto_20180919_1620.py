# Generated by Django 2.1 on 2018-09-19 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_perfil_descricao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analisetalento',
            name='avaliacao',
        ),
        migrations.RemoveField(
            model_name='analisetalento',
            name='nota',
        ),
        migrations.AddField(
            model_name='analisetalento',
            name='nota_curso',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Cursos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='analisetalento',
            name='nota_especializacao',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Especialização'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='analisetalento',
            name='nota_essencia_talento',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Essência/Talento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='analisetalento',
            name='nota_formacao_academica',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Formação Acadêmica'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='analisetalento',
            name='nota_idioma',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Idiomas'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='analisetalento',
            name='nota_performance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Performance'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='analisetalento',
            name='nota_total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Nota Total'),
            preserve_default=False,
        ),
    ]
