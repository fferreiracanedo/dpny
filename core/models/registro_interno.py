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
from django.contrib.auth.models import User


class RegistroInterno(models.Model):
    """
    Classe Registro Interno realiza um registro interno de mensagens/observações no sistema.
    """

    mensagem = models.TextField(
        verbose_name="Mensagem"
    )

    arquivo = models.FileField(
        verbose_name="Arquivo",
        upload_to='registro_interno/',
        blank=True
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="User",
        blank=True,
        null=True
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        default=datetime.now
    )

    def __str__(self):
        return self.mensagem

    class Meta:
        app_label = "core"
        verbose_name = "Registro Interno"
        verbose_name_plural = "Registros Internos"
        ordering = ["-id"]

