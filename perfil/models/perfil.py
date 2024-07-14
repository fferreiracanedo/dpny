from django.db import models
from experiencia_profissional.models import Cargo
from django.contrib.auth.models import User


class Perfil(models.Model):
    NIVEL_ESCOLARIDADE_CHOICES = (
        ('Ensino Médio', 'Ensino Médio'),
        ('Técnico', 'Técnico'),
        ('Graduação', 'Graduação'),
        ('Especialização', 'Especialização'),
        ('Mestrado', 'Mestrado'),
        ('Doutorado', 'Doutorado')
    )

    REQUISITOS_TECNICOS_CHOICES = (
        ('1.0', '1 Ponto'),
        ('2.0', '2 Pontos'),
        ('3.0', '3 Pontos'),
        ('4.0', '4 Pontos'),
        ('5.0', '5 Pontos'),
    )

    IDIOMA_CHOICES = (
        ('1.0', 'Básico'),
        ('2.0', 'Básico a Intermediário'),
        ('3.0', 'Intermediário'),
        ('4.0', 'Avançado'),
        ('5.0', 'Fluente/Nativo'),
    )

    ESPECIALIZACAO_CHOICES = (
        ('2.0', 'Trancado/Não Possui'),
        ('3.0', 'Cursando'),
        ('5.0', 'Concluído'),
    )

    FORMACAO_CHOICES = (
        ('1.0', 'Trancado/Não Possui'),
        ('3.0', 'Cursando'),
        ('5.0', 'Concluído'),
    )

    CURSO_CHOICES = (
        ('1.0', '1 Curso'),
        ('2.0', '2 Cursos'),
        ('3.0', '3 Cursos'),
        ('4.0', '4 Cursos'),
        ('5.0', '5 Cursos'),
    )

    PERFORMANCE_CHOICES = (
        ('1.0', 'Não atinge o esperado'),
        ('2.0', 'As vezes atinge'),
        ('3.0', 'Atinge'),
        ('4.0', 'As vezes supera'),
        ('5.0', 'Sempre supera'),
    )

    EXPERIENCIA_CHOICES = (
        ('1.0', 'Até 1 ano'),
        ('2.0', 'Entre 1 e 2 anos'),
        ('3.0', 'Entre 2 e 3 anos'),
        ('4.0', 'Entre 4 e 5 anos'),
        ('5.0', 'Acima de 5 anos'),
    )

    STATUS_CHOICE = (
        ('Aberta', 'Aberta'),
        ('Encerrada', 'Encerrada'),
        ('Cancelada', 'Cancelada'),
    )

    nome = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        verbose_name="Nome"
    )

    cargo = models.ForeignKey(
        Cargo,
        on_delete=models.CASCADE,
        verbose_name="Cargo"
    )

    visualizar_site = models.BooleanField(
        verbose_name="Disponibilizar no Site?",
        default=False
    )

    visualizar_linkedin = models.BooleanField(
        verbose_name="Disponibilizar no Linkedin?",
        default=False
    )

    visualizar_funcionarios = models.BooleanField(
        verbose_name="Disponibilizar para funcionários?",
        default=False
    )

    salario = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Salário (R$)",
        blank=True,
        null=True
    )

    beneficios = models.TextField(
        verbose_name="Benefícios",
        blank=True,
        null=True
    )

    data_inicio = models.DateField(
        verbose_name="Data de Início",
        blank=True,
        null=True
    )

    data_final = models.DateField(
        verbose_name="Data de Término",
        blank=True,
        null=True
    )

    nota_maxima_requisitos_tecnicos = models.CharField(
        max_length=250,
        choices=REQUISITOS_TECNICOS_CHOICES,
        verbose_name="Nota Máxima para Requisitos Técnicos"
    )

    peso_requisitos_tecnicos = models.IntegerField(
        verbose_name="Peso para Requisitos Técnicos",
        default=1
    )

    nota_maxima_experiencia = models.CharField(
        max_length=250,
        choices=EXPERIENCIA_CHOICES,
        verbose_name="Nota Máxima para Experiência"
    )

    peso_experiencia = models.IntegerField(
        verbose_name="Peso para Experiência",
        default=1
    )

    nota_maxima_formacao_academica = models.CharField(
        max_length=250,
        choices=FORMACAO_CHOICES,
        verbose_name="Nota Máxima para Formação Acadêmica"
    )

    peso_formacao_academica = models.IntegerField(
        verbose_name="Peso para Formação Acadêmica",
        default=1
    )

    nivel_escolaridade_exigido = models.CharField(
        verbose_name="Nível de Escolaridade Exigido", 
        max_length=50,
        choices=NIVEL_ESCOLARIDADE_CHOICES,
        blank=True, null=True
    )

    nota_maxima_cursos = models.CharField(
        max_length=250,
        choices=CURSO_CHOICES,
        verbose_name="Nota Máxima para Cursos"
    )

    peso_cursos = models.IntegerField(
        verbose_name="Peso para Cursos",
        default=1
    )

    nota_maxima_idiomas = models.CharField(
        max_length=250,
        choices=IDIOMA_CHOICES,
        verbose_name="Nota Máxima para Idiomas"
    )

    peso_idiomas = models.IntegerField(
        verbose_name="Peso para Idiomas",
        default=1
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICE,
        verbose_name="Status",
        default='Aberta'
    )

    data_abertura = models.DateField(
        verbose_name="Data de Abertura",
        blank=True, null=True
    )

    template_teste_psicologico = models.ForeignKey(
        "teste_psicologico.TemplateTestePsicologico",
        verbose_name="Template de Teste Escrito",
        on_delete=models.CASCADE,
        blank=True, null=True
    )

    gestor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def gerar_testes(self):
        from teste_psicologico.models import TestePsicologico
        from teste_psicologico.models import Afirmativa

        for analise in self.analisetalento_set.all()[:3]:
            teste_psicologico = TestePsicologico(
                    pessoa=analise.pessoa,
                    perfil=self
                )

            teste_psicologico.save()

            if self.template_teste_psicologico:
                for afirmativa in self.template_teste_psicologico.afirmativa_set.all():
                    nova_afirmativa = Afirmativa(
                        afirmativa=afirmativa.afirmativa,
                        ordem=afirmativa.ordem,
                        teste_psicologico=teste_psicologico
                    )

                    nova_afirmativa.save()
            else:
                for afirmativa in self.afirmativa_set.all():
                    nova_afirmativa = Afirmativa(
                        afirmativa=afirmativa.afirmativa,
                        ordem=afirmativa.ordem,
                        teste_psicologico=teste_psicologico
                    )

                    nova_afirmativa.save()


    def __str__(self):
        return self.nome

    class Meta:
        app_label = "perfil"
        verbose_name = "Vaga"
        verbose_name_plural = "Vagas"
        ordering = ['nome']
