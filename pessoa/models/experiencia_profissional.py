from django.db import models
from experiencia_profissional.models import Experiencia
from experiencia_profissional.models import Cargo
from .pessoa import Pessoa


class ExperienciaProfissional(models.Model):
    empresa = models.CharField(
        verbose_name="Empresa", 
        max_length=150
    )

    cargo = models.ForeignKey(
        Cargo,
        on_delete=models.CASCADE,
        verbose_name="Cargo"
    )

    outro_cargo = models.CharField(
        verbose_name="Outro Cargo", 
        max_length=150,
        null=True, blank=True
    )

    data_inicio = models.DateField(
        verbose_name="Data de Início",
        null=True
    )

    data_termino = models.DateField(
        verbose_name="Data de Término",
        blank=True,
        null=True
    )

    trabalho_atual = models.BooleanField(
        verbose_name="Trabalho Atual?",
        default=False
    )

    tempo = models.ForeignKey(
        Experiencia,
        on_delete=models.CASCADE,
        verbose_name="Tempo de Permanência",
        blank=True,
        null=True
    )

    cargo_atual = models.BooleanField(
        verbose_name="Cargo Atual",
        default=False
    )

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name="Perfil"
    )

    @property
    def tempo_empresa(self):
        from datetime import date
        
        data_termino = self.data_termino if self.data_termino else date.today()

        diferenca = data_termino - self.data_inicio

        dias = diferenca.days
        anos, dias = dias // 365, dias % 365
        meses, dias = dias // 30, dias % 30

        return '{} ano(s) e {} mês(es)'.format(
            anos,
            meses
        )

    @property
    def tempo_experiencia(self):
        from datetime import date

        data_termino = self.data_termino if self.data_termino else date.today()

        diferenca = data_termino - self.data_inicio
        anos = diferenca.days // 365

        return anos

    def __str__(self):
        return self.cargo.titulo

    class Meta:
        app_label = "pessoa"
        verbose_name = "Experiência"
        verbose_name_plural = "Experiências"
        ordering = ['-data_inicio']
