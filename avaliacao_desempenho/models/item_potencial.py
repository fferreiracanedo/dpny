from django.db import models
from configuracao_avaliacao_desempenho.models import Potencial
from .avaliacao_desempenho import AvaliacaoDesempenho


class ItemPotencial(models.Model):
    OPCOES_RESPOSTA = (
        ('NA', 'Avaliação não apropriada no momento (menos de 6 meses na empresa)'),
        ('R-', 'Não satisfatório, devendo ser fruto de análise para atividade de menor complexidade ou desligamento'),
        ('R', 'Situação estável'),
        ('R+', 'Capacidade para crescimento horizontal, atividades mais complexas'),
        ('AP', 'Potencial para crescimento vertical'),
    )
    
    potencial = models.ForeignKey(
        Potencial,
        verbose_name="Potencial",
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
        return self.potencial.potencial

    class Meta:
        app_label = "avaliacao_desempenho"
        verbose_name = "Item de Potencial"
        verbose_name_plural = "Itens de Potenciais"
        ordering = ['potencial']