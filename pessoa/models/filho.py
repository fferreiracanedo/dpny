from django.db import models

from .pessoa import Pessoa


class Filho(models.Model):
    nome = models.CharField(
        max_length=250,
        verbose_name="Nome"
    )

    cpf = models.CharField(
        max_length=14,
        verbose_name="CPF",
        blank=True, null=True,
    )

    cpf_anexo = models.FileField(
        verbose_name="CPF Digitalizado",
        upload_to="documentos/",
        blank=True
    )

    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
        blank=True,
        null=True
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name="Pessoa"
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "pessoa"
        verbose_name = "Filho"
        verbose_name_plural = "Filhos"
