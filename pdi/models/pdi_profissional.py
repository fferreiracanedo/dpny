from django.db import models
from .acao import Acao
from .pdi import Pdi


class PdiProfissional(models.Model):
    acao = models.ForeignKey(
        Acao,
        on_delete=models.CASCADE,
        verbose_name="Ação"
    )

    responsavel = models.CharField(
        max_length=250,
        null=False,
        verbose_name="Responsável"
    )

    prazo = models.CharField(
        max_length=250,
        null=False,
        verbose_name="Prazo"
    )

    metrica = models.CharField(
        max_length=250,
        null=False,
        verbose_name="Métrica"
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
        verbose_name = "PDI - Profissional"
        verbose_name_plural = "PDI - Profissional"
        ordering = ['acao']
