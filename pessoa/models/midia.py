from django.db import models
from .pessoa import Pessoa


class Midia(models.Model):
    titulo = models.CharField(
        verbose_name='Título',
        max_length=150,
        blank=True, null=True
    )

    descricao = models.TextField(
        verbose_name='Descrição',
        blank=True, null=True
    )

    link = models.CharField(
        verbose_name='Link',
        max_length=250,
        blank=True, null=True
    )

    data_criacao = models.DateTimeField(
        verbose_name='Data de Criação',
        blank=True, null=True
    )

    arquivo = models.FileField(
        blank=True
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name="Pessoa"
    )

    def __str__(self):
        return "{}-{}".format(self.id, self.pessoa)

    class Meta:
        app_label = "pessoa"
        verbose_name = "Mídia"
        verbose_name_plural = "Mídias"
