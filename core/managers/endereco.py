__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2019, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from django.db import models
from pycep_correios import consultar_cep


class EnderecoManager(models.Manager):
    """
    Classe Endereco Manager as funções managers relacionadas a um endereço na plataforma.
    """

    def buscar_cep(self, cep):
        from core.models import Cidade
        from core.models import Estado
        from core.models import Pais

        try:
            endereco = consultar_cep(cep)

            pais = Pais.objects.get(pk=1)

            if pais:
                estado = Estado.objects.filter(pais=pais.id, codigo=endereco['uf'])[:1]

                if len(estado) > 0:
                    estado_id = estado[0].id
                    cidade = Cidade.objects.filter(estado=estado_id, nome=endereco['cidade'])[:1]

                    if len(cidade) > 0:
                        cidade_id = cidade[0].id

            data = {
                'logradouro': endereco['end'],
                'bairro': endereco['bairro'],
                'cidade': cidade_id or "",
                'estado': estado_id or "",
                'pais': pais.id or ""
            }

            return data
        except:
            data = {}

        return data

