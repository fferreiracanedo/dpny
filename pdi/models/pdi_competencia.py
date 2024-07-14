from django.db import models
from .acao import Acao
from .pdi import Pdi
from configuracao_avaliacao_desempenho.models import Competencia


class PdiCompetencia(models.Model):
    acao = models.ForeignKey(
        Acao,
        on_delete=models.CASCADE,
        verbose_name="Ação"
    )

    competencia = models.ForeignKey(
        Competencia,
        on_delete=models.CASCADE,
        verbose_name="Competência"
    )

    pdi = models.ForeignKey(
        Pdi,
        on_delete=models.CASCADE,
        verbose_name="PDI"
    )

    def __str__(self):
        return self.acao.nome

    class Meta:
        app_label = "pdi"
        verbose_name = "PDI - Competência"
        verbose_name_plural = "PDI - Competências"
        ordering = ['acao']
