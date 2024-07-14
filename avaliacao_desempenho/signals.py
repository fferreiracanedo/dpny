from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AvaliacaoDesempenho


@receiver(post_save, sender=AvaliacaoDesempenho)
def calcular_quadrante(sender, instance, created, **kwargs):
    if created:
        pass
    else:
        for campo in kwargs['update_fields']:
            if campo == 'respondida' and instance.respondida:
                    instance.calcular_quadrante()

