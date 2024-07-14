__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2019, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from django.db import models
from .estado import Estado
from datetime import datetime


class Cidade(models.Model):
    """
    Classe Cidade implementa as funções relacionadas a uma cidade na plataforma.
    """

    nome = models.CharField(
        max_length=200,
        verbose_name="Nome"
    )

    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        verbose_name="Estado"
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        default=datetime.now
    )

    @property
    def pais(self):
        return self.estado.pais

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "core"
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        ordering = ['estado', 'nome']

