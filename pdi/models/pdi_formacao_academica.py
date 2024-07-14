from django.db import models
from formacao.models import FormacaoAcademica
from formacao.models import Curso
from formacao.models import Instituicao
from .pdi import Pdi


class PdiFormacaoAcademica(models.Model):
    formacao_academica = models.ForeignKey(
        FormacaoAcademica,
        on_delete=models.CASCADE,
        verbose_name="Formação"
    )

    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        verbose_name="Curso"
    )

    instituicao = models.ForeignKey(
        Instituicao,
        on_delete=models.CASCADE,
        verbose_name="Instituição"
    )

    prazo = models.CharField(
        max_length=250,
        null=False,
        verbose_name="Prazo"
    )

    pdi = models.ForeignKey(
        Pdi,
        on_delete=models.CASCADE,
        verbose_name="PDI"
    )

    def __str__(self):
        return self.formacao_academica.titulo

    class Meta:
        app_label = "pdi"
        verbose_name = "PDI - Formação Acadêmica"
        verbose_name_plural = "PDI - Formação Acadêmica"
        ordering = ['formacao_academica']
