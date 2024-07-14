__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2019, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from django.db import models
from datetime import datetime


class Filial(models.Model):
    """
    Classe Filial implementa as funções relacionadas a uma filial na plataforma.
    """

    nome = models.CharField(
        max_length=200,
        verbose_name="Nome"
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        default=datetime.now
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "core"
        verbose_name = "Filial"
        verbose_name_plural = "Filiais"
        ordering = ['nome']

