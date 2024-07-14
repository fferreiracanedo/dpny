from django.db import models


class RequisitoTecnico(models.Model):
    nome = models.CharField(
        max_length=150,
        blank=False
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "pessoa"
        verbose_name = "Requisito Técnico"
        verbose_name_plural = "Requisitos Técnicos"
        ordering = ['nome']