from django import template
from teste_psicologico.models import Resposta

register = template.Library()


@register.simple_tag
def number_format(number):
    return "{}".format(number).replace(',', '.')


@register.simple_tag
def buscar_resposta(perfil, pessoa):
    resposta = Resposta.objects.filter(
        teste_psicologico__perfil__id=perfil, 
        teste_psicologico__pessoa__id=pessoa
    ).first()

    return resposta.id if resposta else False
