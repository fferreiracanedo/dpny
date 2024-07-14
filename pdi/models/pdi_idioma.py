from django.db import models
from formacao.models import Idioma
from .pdi import Pdi


class PdiIdioma(models.Model):
    idioma = models.ForeignKey(
        Idioma,
        on_delete=models.CASCADE,
        verbose_name="Idioma"
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
        return self.idioma.titulo

    class Meta:
        app_label = "pdi"
        verbose_name = "PDI - Idioma"
        verbose_name_plural = "PDI - Idioma"
        ordering = ['idioma']
