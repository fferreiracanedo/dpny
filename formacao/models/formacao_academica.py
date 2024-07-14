from django.db import models


class FormacaoAcademica(models.Model):
    titulo = models.CharField(
        max_length=150,
        null=False,
        verbose_name="Título"
    )

    pontos = models.IntegerField(

    )

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = "formacao"
        verbose_name = "Formação Acadêmica"
        verbose_name_plural = "Formações Acadêmicas"
        ordering = ['titulo']
