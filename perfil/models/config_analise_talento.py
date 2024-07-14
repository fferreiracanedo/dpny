from django.db import models
from experiencia_profissional.models import Cargo


class ConfigAnaliseTalento(models.Model):

    nome = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        verbose_name="Nome"
    )

    maximo_analises = models.IntegerField(verbose_name="Número Máximo de Análises")

    quantidade_atual_analises = models.IntegerField(verbose_name="Número Atual de Análises")

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "perfil"
        verbose_name = "Configuração de Análise de Talento"
        verbose_name_plural = "Configurações de Análise de Talento"
