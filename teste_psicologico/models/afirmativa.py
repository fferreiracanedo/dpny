from django.db import models
from .template_teste_psicologico import TemplateTestePsicologico
from .teste_psicologico import TestePsicologico
from perfil.models import Perfil


class Afirmativa(models.Model):
    afirmativa = models.TextField(
        null=False,
        verbose_name="Afirmativa"
    )
    
    ordem = models.IntegerField(

    )

    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        verbose_name="Perfil",
        blank=True, null=True
    )

    template_teste_psicologico = models.ForeignKey(
        TemplateTestePsicologico,
        verbose_name="Template de Teste Psicológico",
        on_delete=models.CASCADE,
        blank=True, null=True
    )

    teste_psicologico = models.ForeignKey(
        TestePsicologico,
        verbose_name="Teste Psicológico",
        on_delete=models.CASCADE,
        blank=True, null=True
    )

    def __str__(self):
        return self.afirmativa[0:100]+"..."

    class Meta:
        app_label = "teste_psicologico"
        verbose_name = "Afirmativa"
        verbose_name_plural = "Afirmativas"
        ordering = ['ordem']
