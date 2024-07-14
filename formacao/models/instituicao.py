from django.db import models


class Instituicao(models.Model):
    nome = models.CharField(
        max_length=150,
        null=False,
        verbose_name="Nome"
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "formacao"
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"
        ordering = ['nome']
