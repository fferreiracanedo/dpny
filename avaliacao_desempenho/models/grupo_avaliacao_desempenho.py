__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2019, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from django.db import models
from django.contrib.auth.models import User
from configuracao_avaliacao_desempenho.models import Competencia
from configuracao_avaliacao_desempenho.models import Potencial
from pessoa.models import Pessoa
from datetime import datetime


class GrupoAvaliacaoDesempenho(models.Model):
    """
    Classe Grupo Avaliação de Desempenho implementa as funções relacionadas a uma rotina de avaliações de desempenho
    na plataforma, controlando a geração das avaliações individuais.
    """
    nome = models.CharField(
        max_length=200,
        verbose_name="Nome"
    )

    data_inicial = models.DateField(
        verbose_name="Data Inicial"
    )

    data_final = models.DateField(
        verbose_name="Data Final"
    )

    descricao = models.TextField(
        verbose_name="Descrição"
    )

    pessoa = models.ManyToManyField(
        Pessoa,
        verbose_name="Pessoa"
    )

    competencia = models.ManyToManyField(
        Competencia,
        verbose_name="Competências",
        blank=True, null=True,
    )

    ja_gerado = models.BooleanField(
        verbose_name="Avaliações já Geradas",
        default=False
    )

    data_criacao = models.DateTimeField(
        verbose_name="Data de Criação",
        default=datetime.now
    )

    def gerar_avaliacoes(self):
        # Rodar todos as pessoas para gerar uma avaliação para cada
        if not self.ja_gerado:
            for pessoa in self.pessoa.all():
                # Gerando a Autoavaliação
                self.gerar_avaliacao_individual(pessoa, pessoa.user, 'autoavaliacao')

                # Gerando a Avaliação do Gestor
                if pessoa.gestor:
                    self.gerar_avaliacao_individual(pessoa.gestor.pessoa, pessoa.user, 'gestor')

                # Gerando a Avaliação dos Subordinados
                subordinados = Pessoa.objects.filter(gestor=pessoa.user)
                for subordinado in subordinados:
                    self.gerar_avaliacao_individual(subordinado, pessoa.user, 'subordinado')

                # Gerando a Avaliação dos Pares
                for par in pessoa.pessoa_set.all():
                    self.gerar_avaliacao_individual(par, pessoa.user, 'par')
            
            self.ja_gerado = True
            self.save()

    def gerar_avaliacao_individual(self, pessoa, avaliador, tipo_avaliacao):
        from .avaliacao_desempenho import AvaliacaoDesempenho
        from datetime import date

        avaliacao_desempenho = AvaliacaoDesempenho.objects.create(
            pessoa=pessoa,
            avaliador=avaliador,
            data=date.today(),
            tipo_avaliacao=tipo_avaliacao
        )

        self.gerar_competencias(avaliacao_desempenho)
    
    def gerar_competencias(self, avaliacao_desempenho):
        from .item_competencia import ItemCompetencia

        for competencia in self.competencia.all():
            if competencia.categoria == 'liderado' and not avaliacao_desempenho.pessoa.is_lider or competencia.categoria == 'lider' and avaliacao_desempenho.pessoa.is_lider:
                ItemCompetencia.objects.create(
                    competencia=competencia,
                    avaliacao_desempenho=avaliacao_desempenho
                )


    def __str__(self):
        return self.nome

    class Meta:
        app_label = "avaliacao_desempenho"
        verbose_name = "Grupo de Avaliação"
        verbose_name_plural = "Grupos de Avaliações"

