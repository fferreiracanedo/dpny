from django.db import models
from formacao.models import FormacaoAcademica
from formacao.models import AnoFormacao
from .pessoa import Pessoa


class FormacaoAcademica(models.Model):
    NIVEL_ESCOLARIDADE_CHOICES = (
        ('Ensino Fundamental', 'Ensino Fundamental'),
        ('Ensino Médio', 'Ensino Médio'),
        ('Técnico', 'Técnico'),
        ('Graduação', 'Graduação'),
        ('Especialização', 'Especialização'),
        ('Mestrado', 'Mestrado'),
        ('Doutorado', 'Doutorado')
    )

    SITUACAO_CHOICES = (
        ('Concluído', 'Concluído'),
        ('Cursando', 'Cursando'),
        ('Trancado', 'Incompleto')
    )

    nivel_escolaridade = models.CharField(
        verbose_name="Nível de Escolaridade", 
        max_length=50,
        choices=NIVEL_ESCOLARIDADE_CHOICES
    )
    
    curso = models.ForeignKey(
        "formacao.Curso",
        on_delete=models.CASCADE,
        verbose_name="Curso"
    )

    outro_curso = models.CharField(
        verbose_name="Outro Curso", 
        max_length=150,
        null=True, blank=True
    )

    instituicao = models.CharField(
        verbose_name="Instituição", 
        max_length=150,
        null=True
    )

    situacao = models.CharField(
        verbose_name="Situação", 
        max_length=50,
        choices=SITUACAO_CHOICES
    )

    data_inicio = models.DateField(
        verbose_name="Data de Início",
        null=True
    )

    data_termino = models.DateField(
        verbose_name="Data de Término",
        blank=True,
        null=True
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name="Pessoa"
    )

    certificado = models.FileField(
        verbose_name="Certificado",
        blank=True
    )

    def __str__(self):
        return "{} - {}".format(self.curso, self.instituicao)

    class Meta:
        app_label = "pessoa"
        verbose_name = "Formação Acadêmica"
        verbose_name_plural = "Formações Acadêmicas"
        ordering = ['-data_inicio']
