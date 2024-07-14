from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
from .perfil import Perfil
from pessoa.models import Pessoa
from teste_psicologico.models import TestePsicologico
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from decouple import config
from django.utils.html import strip_tags


class AnaliseTalento(models.Model):

    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name="Pessoa"
    )

    perfil = models.ForeignKey(
        Perfil,
        on_delete=models.CASCADE,
        verbose_name="Perfil"
    )

    nota_requisitos_tecnicos = models.CharField(
        max_length=30,
        verbose_name="Requisitos Técnicos"
    )

    nota_experiencia = models.CharField(
        max_length=30,
        verbose_name="Experiência"
    )

    nota_formacao_academica = models.CharField(
        max_length=30,
        verbose_name="Formação Acadêmica"
    )

    nota_curso = models.CharField(
        max_length=30,
        verbose_name="Cursos"
    )

    nota_idioma = models.CharField(
        max_length=30,
        verbose_name="Idiomas"
    )

    nota_total = models.CharField(
        max_length=30,
        verbose_name="Nota Total"
    )

    def email_confirmacao(self):
        html_text = render_to_string('analises/email_confirmacao.html', {'perfil': self.perfil})
        text = strip_tags(html_text)

        email = EmailMessage(
            'Candidatura efetuada com sucesso!', text, config('EMAIL_HOST_USER'),
            [self.pessoa.email])

        email.send()
    
    def save(self, *args, **kwargs):
        if self.pk:
            # If self.pk is not None then it's an update.
            cls = self.__class__
            old = cls.objects.get(pk=self.pk)
            # This will get the current model state since super().save() isn't called yet.
            new = self  # This gets the newly instantiated Mode object with the new values.
            changed_fields = []
            for field in cls._meta.get_fields():
                field_name = field.name
                try:
                    if getattr(old, field_name) != getattr(new, field_name):
                        changed_fields.append(field_name)
                except Exception as ex:  # Catch field does not exist exception
                    pass
            kwargs['update_fields'] = changed_fields
        super().save(*args, **kwargs)

    @property
    def resposta_teste(self):
        from teste_psicologico.models import TestePsicologico

        teste_psicologico = TestePsicologico.objects.filter(
            perfil__id=self.perfil.id, 
            pessoa__id=self.pessoa.id,
            respondido=True
        ).first()

        return teste_psicologico

    def __str__(self):
        return self.pessoa.nome

    class Meta:
        app_label = "perfil"
        verbose_name = "Análise de Talento"
        verbose_name_plural = "Análises de Talentos"
        ordering = ['-nota_total']

    def formatar_nota(self, nota, maximo):
        nota = float(nota)
        maximo = float(maximo)

        if nota > maximo:
            nota = maximo

        try:
            porcentagem = nota / maximo * 100
            return "{:.2f}/{:.2f} = {:.2f}%".format(nota, maximo, porcentagem)
        except ZeroDivisionError:
            return "0.00/0.00 = 0.00%"
    
    def calcular_nota_requisitos_tecnicos(self):
        somatorio = 0

        for requisito_tecnico in self.pessoa.requisitos_tecnicos.all():
            if requisito_tecnico in self.perfil.cargo.requisitos_tecnicos.all():
                somatorio += 1
        
        nota_requisitos_tecnicos = self.formatar_nota(
            somatorio*self.perfil.peso_requisitos_tecnicos, 
            float(self.perfil.nota_maxima_requisitos_tecnicos)*self.perfil.peso_requisitos_tecnicos
        )

        if self.nota_requisitos_tecnicos != nota_requisitos_tecnicos:
            self.nota_requisitos_tecnicos = nota_requisitos_tecnicos
            self.save()



    def calcular_nota_experiencia(self):
        somatorio_experiencia = 0
        for experiencia in self.pessoa.experienciaprofissional_set.all():
            if experiencia.cargo.area_atuacao == self.perfil.cargo.area_atuacao:
                somatorio_experiencia += experiencia.tempo_experiencia + 1

        nota_experiencia = self.formatar_nota(
            somatorio_experiencia*self.perfil.peso_experiencia, 
            float(self.perfil.nota_maxima_experiencia)*self.perfil.peso_experiencia
        )

        if self.nota_experiencia != nota_experiencia:
            self.nota_experiencia = nota_experiencia
            self.save()

    def calcular_nota_formacao_academica(self):
        somatorio_formacao_academica = 0

        for formacao in self.pessoa.formacaoacademica_set.all():
            if formacao.curso.area_atuacao == self.perfil.cargo.area_atuacao:
                if self.perfil.nivel_escolaridade_exigido:
                    if formacao.nivel_escolaridade == self.perfil.nivel_escolaridade_exigido:
                        if formacao.situacao == 'Concluído':
                            somatorio_formacao_academica += 5
                        elif formacao.situacao == 'Cursando':
                            somatorio_formacao_academica += 3
                        elif formacao.situacao == 'Trancado':
                            somatorio_formacao_academica += 1
                else:
                    if formacao.situacao == 'Concluído':
                        somatorio_formacao_academica += 5
                    elif formacao.situacao == 'Cursando':
                        somatorio_formacao_academica += 3
                    elif formacao.situacao == 'Trancado':
                        somatorio_formacao_academica += 1

        nota_formacao_academica = self.formatar_nota(
            somatorio_formacao_academica*self.perfil.peso_formacao_academica, 
            float(self.perfil.nota_maxima_formacao_academica)*self.perfil.peso_formacao_academica
        )

        if self.nota_formacao_academica != nota_formacao_academica:
            self.nota_formacao_academica = nota_formacao_academica
            self.save()

    def calcular_nota_curso(self):
        somatorio_curso = len(self.pessoa.curso_set.all())

        nota_curso = self.formatar_nota(
            somatorio_curso*self.perfil.peso_cursos, 
            float(self.perfil.nota_maxima_cursos)*self.perfil.peso_cursos
        )

        if self.nota_curso != nota_curso:
            self.nota_curso = nota_curso
            self.save()

    def calcular_nota_idiomas(self):
        somatorio_idiomas = 0

        for idioma in self.pessoa.idioma_set.all():
            somatorio_idiomas += idioma.pontuacao

        nota_idioma = self.formatar_nota(
            somatorio_idiomas*self.perfil.peso_idiomas, 
            float(self.perfil.nota_maxima_idiomas)*self.perfil.peso_idiomas
        )

        if self.nota_idioma != nota_idioma:
            self.nota_idioma = nota_idioma
            self.save()

    def calcular_nota_total(self):
        somatorio_nota_total = 0
        somatorio_nota_maxima_total = 0

        somatorio_nota_total += float(self.nota_requisitos_tecnicos.split("/")[0])
        somatorio_nota_total += float(self.nota_experiencia.split("/")[0])
        somatorio_nota_total += float(self.nota_formacao_academica.split("/")[0])
        somatorio_nota_total += float(self.nota_curso.split("/")[0])
        somatorio_nota_total += float(self.nota_idioma.split("/")[0])

        somatorio_nota_maxima_total += float(self.perfil.nota_maxima_requisitos_tecnicos)*self.perfil.peso_requisitos_tecnicos
        somatorio_nota_maxima_total += float(self.perfil.nota_maxima_experiencia)*self.perfil.peso_experiencia
        somatorio_nota_maxima_total += float(self.perfil.nota_maxima_formacao_academica)*self.perfil.peso_formacao_academica
        somatorio_nota_maxima_total += float(self.perfil.nota_maxima_cursos)*self.perfil.peso_cursos
        somatorio_nota_maxima_total += float(self.perfil.nota_maxima_idiomas)*self.perfil.peso_idiomas

        nota_total = self.formatar_nota(somatorio_nota_total, somatorio_nota_maxima_total)

        if self.nota_total != nota_total:
            self.nota_total = nota_total
            self.save()


@receiver(post_save, sender=AnaliseTalento)
def update_valor_pago(sender, instance, **kwargs):
    instance.calcular_nota_requisitos_tecnicos()
    instance.calcular_nota_experiencia()
    instance.calcular_nota_formacao_academica()
    instance.calcular_nota_curso()
    instance.calcular_nota_idiomas()
    instance.calcular_nota_total()