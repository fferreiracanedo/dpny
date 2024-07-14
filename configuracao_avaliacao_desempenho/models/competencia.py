from django.db import models


class Competencia(models.Model):
    OPCOES_TIPO = (
        ('N', 'Negócios'),
        ('P', 'Pessoas')
    )

    OPCOES_CATEGORIA = (
        ('lider', 'Líder'),
        ('liderado', 'Liderado')
    )
    
    competencia = models.CharField(
        verbose_name="Competência",
        max_length=250
    )

    explicativo = models.TextField(
        verbose_name="Explicativo",
        blank=True, null=True
    )

    tipo = models.CharField(
        verbose_name="Tipo",
        max_length=1,
        choices=OPCOES_TIPO
    )

    categoria = models.CharField(
        verbose_name="Categoria",
        max_length=15,
        choices=OPCOES_CATEGORIA,
        default='liderado'
    )

    autoavaliacao = models.BooleanField(
        verbose_name="Autoavaliação",
        default=False
    )

    gestor = models.BooleanField(
        verbose_name="Gestor",
        default=False
    )

    subordinado = models.BooleanField(
        verbose_name="Subordinado",
        default=False
    )

    par = models.BooleanField(
        verbose_name="Par",
        default=False
    )

    exibir_titulo = models.BooleanField(
        verbose_name="Exibir o Título",
        default=False
    )

    explicativo_titulo = models.TextField(
        verbose_name="Explicativo do Título",
        blank=True, null=True
    )

    ordem = models.IntegerField(
        verbose_name="Ordem",
        default=0
    )
    
    def __str__(self):
        return "{} - {}".format(self.competencia, self.explicativo)

    class Meta:
        app_label = "configuracao_avaliacao_desempenho"
        verbose_name = "Competência"
        verbose_name_plural = "Competências"
        ordering = ['ordem']