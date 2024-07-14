from django.db import models


class Potencial(models.Model):
    potencial = models.CharField(
        verbose_name="Potencial",
        max_length=250
    )

    explicativo = models.TextField(
        verbose_name="Explicativo",
        blank=True, null=True
    )
    
    def __str__(self):
        return self.potencial

    class Meta:
        app_label = "configuracao_avaliacao_desempenho"
        verbose_name = "Potencial"
        verbose_name_plural = "Potenciais"
        ordering = ['potencial']