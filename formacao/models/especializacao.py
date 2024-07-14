from django.db import models


class Especializacao(models.Model):
    titulo = models.CharField(
        max_length=150,
        null=False,
        verbose_name="Título"
    )

    pontos = models.IntegerField(

    )

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = "formacao"
        verbose_name = "Especialização"
        verbose_name_plural = "Especializações"
        ordering = ['titulo']
