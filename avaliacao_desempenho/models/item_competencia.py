from django.db import models
from configuracao_avaliacao_desempenho.models import Competencia
from .avaliacao_desempenho import AvaliacaoDesempenho


class ItemCompetencia(models.Model):
    OPCOES_RESPOSTA = (
        ('RA', 'Raramente'),
        ('OC', 'Ocasionalmente'),
        ('CO', 'Constantemente'),
        ('EX', 'Exacerbadamente'),
    )
    
    competencia = models.ForeignKey(
        Competencia,
        verbose_name="Competência",
        on_delete=models.CASCADE
    )

    resposta = models.CharField(
        verbose_name="Resposta",
        max_length=2,
        choices=OPCOES_RESPOSTA,
        blank=True, null=True
    )

    nota = models.IntegerField(
        verbose_name="Nota",
        blank=True, null=True
    )

    avaliacao_desempenho = models.ForeignKey(
        AvaliacaoDesempenho,
        verbose_name="Avaliação de Desempenho",
        on_delete=models.CASCADE,
        null=True
    )
    
    def __str__(self):
        return self.competencia.competencia

    class Meta:
        app_label = "avaliacao_desempenho"
        verbose_name = "Item de Competência"
        verbose_name_plural = "Itens de Competências"
        ordering = ['competencia']