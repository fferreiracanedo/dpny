from django.db import models
from experiencia_profissional.models import AreaAtuacao


class Curso(models.Model):
    titulo = models.CharField(
        max_length=150,
        null=False,
        verbose_name="Título"
    )

    area_atuacao = models.ForeignKey(
        AreaAtuacao,
        on_delete=models.CASCADE,
        verbose_name="Área de Atuação"
    )

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = "formacao"
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['titulo']
