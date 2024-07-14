from django.db import models
from .area_atuacao import AreaAtuacao
#from pessoa.models import RequisitoTecnico


class Cargo(models.Model):
    titulo = models.CharField(
        max_length=150,
        null=False,
        verbose_name="Título"
    )

    codigo = models.CharField(
        max_length=30,
        blank=True, null=True,
        verbose_name="Código"
    )

    atividades = models.TextField(
        verbose_name="Atividades",
        blank=True, null=True
    )

    responsabilidades = models.TextField(
        verbose_name="Responsabilidades",
        blank=True, null=True
    )

    missao = models.TextField(
        verbose_name="Missão",
        blank=True, null=True
    )

    observacoes = models.TextField(
        verbose_name="Observações",
        blank=True, null=True
    )

    area_atuacao = models.ForeignKey(
        AreaAtuacao,
        on_delete=models.CASCADE,
        verbose_name="Área de Atuação"
    )

    requisitos_tecnicos = models.ManyToManyField(
        'pessoa.RequisitoTecnico',
        verbose_name="Requisitos Técnicos",
        blank=True
    )

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = "experiencia_profissional"
        ordering = ['titulo']
