from django.db import models


class Idioma(models.Model):
    NIVEL_CHOICES = (
        ('BAS', 'Básico'),
        ('BAI', 'Básico a Intermediário'),
        ('INT', 'Intermediário'),
        ('AVA', 'Avançado'),
        ('FLU', 'Fluente/Nativo'),
    )

    idioma = models.CharField(
        max_length=150,
        null=False,
        verbose_name="Idioma"
    )

    pessoa = models.ForeignKey(
        "pessoa.Pessoa",
        on_delete=models.CASCADE,
        verbose_name="Pessoa"
    )

    nivel = models.CharField(
        max_length=3,
        blank=False,
        choices=NIVEL_CHOICES,
        default='BAS',
        verbose_name="Nível"
    )

    certificado = models.FileField(
        blank=True
    )

    @property
    def pontuacao(self):
        if self.nivel == 'BAS':
            return 1
        elif self.nivel == 'BAI':
            return 2
        elif self.nivel == 'INT':
            return 3
        elif self.nivel == 'AVA':
            return 4
        elif self.nivel == 'FLU':
            return 5

    def __str__(self):
        return self.idioma + " - " + self.nivel

    class Meta:
        app_label = "formacao"
        ordering = ['id']
