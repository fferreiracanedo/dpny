from django.db import models
from formacao.models import Curso
from formacao.models import Instituicao
from .pdi import Pdi


class PdiCurso(models.Model):
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
        return self.curso.titulo

    class Meta:
        app_label = "pdi"
        verbose_name = "PDI - Curso"
        verbose_name_plural = "PDI - Curso"
        ordering = ['curso']
