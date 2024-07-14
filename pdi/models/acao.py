from django.db import models


class Acao(models.Model):
    nome = models.CharField(
        max_length=250,
        null=False,
        verbose_name="Nome"
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "pdi"
        verbose_name = "Ação"
        verbose_name_plural = "Ações"
        ordering = ['nome']
