from django.db import models
from .avaliacao_desempenho import AvaliacaoDesempenho
#from avaliacao_desempenho.models import GrupoAvaliacaoDesempenho


class ItemMeta(models.Model):
    OPCOES_FORMA_MEDICAO = (
        ('QT', 'Quantitativa'),
        ('QA', 'Qualitativa')
    )
    
    meta = models.TextField(
        verbose_name="Meta",
    )

    peso = models.DecimalField(
        verbose_name="Peso",
        max_digits=5,
        decimal_places=2
    )

    explicativo = models.TextField(
        verbose_name="Explicativo",
        blank=True, null=True
    )

    resultado_esperado = models.DecimalField(
        verbose_name="Resultado Esperado",
        max_digits=5,
        decimal_places=2
    )

    resultado_atingido = models.DecimalField(
        verbose_name="Resultado Atingido",
        max_digits=5,
        decimal_places=2
    )

    atingimento = models.DecimalField(
        verbose_name="Atingimento",
        max_digits=5,
        decimal_places=2
    )

    forma_medicao = models.CharField(
        verbose_name="Forma de Medição",
        max_length=2,
        choices=OPCOES_FORMA_MEDICAO
    )

    resposta = models.CharField(
        verbose_name="Resposta",
        max_length=2,
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

    @property
    def resultado(self):
        try:
            return self.resultado_atingido / self.resultado_esperado * 100
        except:
            return None

    def __str__(self):
        return self.meta

    class Meta:
        app_label = "avaliacao_desempenho"
        verbose_name = "Item de Meta"
        verbose_name_plural = "Itens de Metas"