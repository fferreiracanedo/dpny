from django.db import models


class Experiencia(models.Model):
    experiencia = models.CharField(
        max_length=150,
        null=False,
        verbose_name="Experiência"
    )

    pontos = models.IntegerField(

    )

    def __str__(self):
        return self.experiencia

    class Meta:
        app_label = "experiencia_profissional"
        verbose_name = "Experiência"
        verbose_name_plural = "Experiências"
        ordering = ['experiencia']
