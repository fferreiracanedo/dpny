from django.db import models

from .pessoa import Pessoa


class Projeto(models.Model):
    projeto = models.CharField(
        max_length=150,
        verbose_name="Projeto"
    )

    data_inicio = models.DateField(
        verbose_name="Data de Início",
        blank=True,
        null=True
    )

    data_final = models.DateField(
        verbose_name="Data de Término",
        blank=True,
        null=True
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name="Pessoa"
    )

    def __str__(self):
        return self.projeto

    class Meta:
        app_label = "pessoa"
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"
