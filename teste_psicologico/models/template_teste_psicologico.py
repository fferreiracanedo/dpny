from django.db import models
from pessoa.models import Pessoa
from perfil.models import Perfil


class TemplateTestePsicologico(models.Model):
    nome = models.CharField(
        verbose_name="Nome",
        max_length=150
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "teste_psicologico"
        verbose_name = "Template de Teste Escrito"
        verbose_name_plural = "Templates de Testes Escritos"