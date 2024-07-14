from django.db import models
from pessoa.models import Pessoa
from django.template.loader import render_to_string
from easy_pdf import rendering
from django.db.models.signals import post_save
from django.dispatch import receiver


class Pdi(models.Model):
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name="Pessoa"
    )

    def enviar_email(self):
        from django.utils.html import strip_tags

        html_text = render_to_string('texto_email.html')
        text = strip_tags(html_text)
        from django.core.mail import EmailMessage


        context = {
            'pdi': self,
        }

        email = EmailMessage(
            'PDI - Gestor de RH', text, 'edson.junior@outboxsistemas.com', ['erikaragghi@gmail.com','edsondelimajunior@gmail.com'])
        email.attach('PDI.pdf',
                     rendering.render_to_pdf('reports/pdf_pdi.html', context=context),
                     'application/pdf')
        email.send()

    def __str__(self):
        return self.pessoa.nome

    class Meta:
        app_label = "pdi"
        verbose_name = "PDI"
        verbose_name_plural = "PDI"