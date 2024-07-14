from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Pessoa


@receiver(post_save, sender=Pessoa)
def nova_pessoa(sender, instance, created, **kwargs):
    if created:
        instance.email_boas_vindas()
