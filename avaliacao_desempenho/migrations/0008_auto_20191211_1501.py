# Generated by Django 2.1.1 on 2019-12-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao_desempenho', '0007_itempotencial_avaliacao_desempenho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcompetencia',
            name='nota',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nota'),
        ),
        migrations.AlterField(
            model_name='itemcompetencia',
            name='resposta',
            field=models.CharField(blank=True, choices=[('RA', 'Raramente'), ('OC', 'Ocasionalmente'), ('CO', 'Constantemente'), ('EX', 'Exacerbadamente')], max_length=2, null=True, verbose_name='Resposta'),
        ),
        migrations.AlterField(
            model_name='itempotencial',
            name='nota',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nota'),
        ),
        migrations.AlterField(
            model_name='itempotencial',
            name='resposta',
            field=models.CharField(blank=True, choices=[('NA', 'Avaliação não apropriada no momento (menos de 6 meses na empresa)'), ('R-', 'Não satisfatório, devendo ser fruto de análise para atividade de menor complexidade ou desligamento'), ('R', 'Situação estável'), ('R+', 'Capacidade para crescimento horizontal, atividades mais complexas'), ('AP', 'Potencial para crescimento vertical')], max_length=2, null=True, verbose_name='Resposta'),
        ),
    ]