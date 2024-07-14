from django.db import models


class AnoFormacao(models.Model):
    ano = models.CharField(
        max_length=150,
        null=False,
        verbose_name="Ano"
    )

    def __str__(self):
        return self.ano

    class Meta:
        app_label = "formacao"
        verbose_name = "Ano de Formação"
        verbose_name_plural = "Anos de Formação"
        ordering = ['ano']
