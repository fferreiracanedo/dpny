from django.db import models


class CargaHoraria(models.Model):
    horas = models.CharField(
        max_length=150,
        null=False,
        verbose_name="Horas"
    )

    pontos = models.IntegerField(

    )

    def __str__(self):
        return self.horas

    class Meta:
        app_label = "formacao"
        verbose_name = "Carga Horária"
        verbose_name_plural = "Cargas Horárias"
        ordering = ['horas']
