from django.db import models
#from avaliacao_desempenho.models import GrupoAvaliacaoDesempenho


class Meta(models.Model):
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

    forma_medicao = models.CharField(
        verbose_name="Forma de Medição",
        max_length=2,
        choices=OPCOES_FORMA_MEDICAO
    )

    grupo_avaliacao_desempenho = models.ForeignKey(
        'avaliacao_desempenho.GrupoAvaliacaoDesempenho',
        verbose_name="Grupo de Avaliação de Desempenho",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.meta

    class Meta:
        app_label = "configuracao_avaliacao_desempenho"
        verbose_name = "Meta"
        verbose_name_plural = "Metas"
        ordering = ['meta']