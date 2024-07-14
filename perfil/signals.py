from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AnaliseTalento


@receiver(post_save, sender=AnaliseTalento)
def nova_analise_talento(sender, instance, created, **kwargs):
    if created:
        instance.email_confirmacao()
