from django.db import models
from formacao.models import Curso
from formacao.models import CargaHoraria
from formacao.models import Instituicao
from .pessoa import Pessoa


class Curso(models.Model):
    curso = models.CharField(
        verbose_name="Curso", 
        max_length=150,
        null=True
    )

    instituicao = models.CharField(
        verbose_name="Instituição", 
        max_length=150,
        null=True
    )

    carga_horaria = models.CharField(
        verbose_name="Carga Horária", 
        max_length=150,
        null=True
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
        blank=True
    )

    def __str__(self):
        return self.curso

    class Meta:
        app_label = "pessoa"
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['-data_inicio']
