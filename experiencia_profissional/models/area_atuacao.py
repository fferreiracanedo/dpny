from django.db import models


class AreaAtuacao(models.Model):
    nome = models.CharField(
        max_length=150,
        null=False,
        verbose_name="Área de Atuação"
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "experiencia_profissional"
        verbose_name = "Área de Atuação"
        verbose_name_plural = "Áreas de Atuação"
        ordering = ['nome']
