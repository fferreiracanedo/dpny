from django.db import models
from formacao.models import Especializacao
from formacao.models import AnoFormacao
from formacao.models import Instituicao
from formacao.models import Curso
from .pessoa import Pessoa


class Especializacao(models.Model):
    especializacao = models.ForeignKey(
        Especializacao,
        on_delete=models.CASCADE,
        verbose_name="Especialização"
    )

    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        verbose_name="Curso"
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name="Perfil"
    )

    certificado = models.FileField(
        blank=True
    )

    def __str__(self):
        return self.especializacao.titulo

    class Meta:
        app_label = "pessoa"
        verbose_name = "Especialização"
        verbose_name_plural = "Especializações"
