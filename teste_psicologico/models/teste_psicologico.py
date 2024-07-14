from django.db import models
from pessoa.models import Pessoa
from perfil.models import Perfil


class TestePsicologico(models.Model):
    OPCOES_AVALIACAO = (
        ('n/a', 'Não Avaliado'),
        ('aprovado', 'Aprovado'),
        ('reprovado', 'Reprovado'),
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name="Pessoa"
    )

    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        verbose_name="Perfil",
        null=True
    )

    respondido = models.BooleanField(
        verbose_name="Teste Respondido",
        default=False
    )
    
    aprovado_gestor = models.CharField(
        verbose_name="Teste Aprovado",
        max_length=10,
        choices=OPCOES_AVALIACAO,
        default='n/a'
    )

    marcar_entrevista = models.BooleanField(
        verbose_name="Marcar Entrevista",
        default=False
    )

    def __str__(self):
        return "{} - {}".format(self.perfil.nome, self.pessoa.nome)

    class Meta:
        app_label = "teste_psicologico"
        verbose_name = "Teste Escrito"
        verbose_name_plural = "Testes Escritos"