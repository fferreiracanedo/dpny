from django.db import models


class CompetenciaProfissional(models.Model):
    nome = models.CharField(
        max_length=150,
        blank=False
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "pessoa"
        verbose_name = "Competência Profissional"
        verbose_name_plural = "Competências Profissionais"