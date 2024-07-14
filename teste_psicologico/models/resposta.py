from django.db import models
from .teste_psicologico import TestePsicologico
from .afirmativa import Afirmativa


class Resposta(models.Model):
    afirmativa = models.ForeignKey(
        Afirmativa,
        on_delete=models.CASCADE,
        verbose_name="Afirmativa"
    )

    resposta = models.TextField(
        verbose_name="Resposta",
        blank=True, null=True
    )

    midia = models.FileField(
        verbose_name="Mídia",
        blank=True, null=True
    )

    teste_psicologico = models.ForeignKey(
        TestePsicologico,
        on_delete=models.CASCADE,
        verbose_name="Teste Psicológico"
    )

    def __str__(self):
        return self.afirmativa.afirmativa

    class Meta:
        app_label = "teste_psicologico"
        verbose_name = "Resposta"
        verbose_name_plural = "Respostas"
        ordering = ['afirmativa']