__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2019, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from avaliacao_desempenho.models import AvaliacaoDesempenho
from avaliacao_desempenho.models import ItemCompetencia
from avaliacao_desempenho.models import ItemMeta
from avaliacao_desempenho.models import ItemPotencial

class AvaliacaoDesempenhoSerializer(ModelSerializer):
    class Meta:
        model = AvaliacaoDesempenho
        fields = '__all__'

class ItemCompetenciaSerializer(ModelSerializer):
    class Meta:
        model = ItemCompetencia
        fields = '__all__'

class ItemMetaSerializer(ModelSerializer):
    class Meta:
        model = ItemMeta
        fields = '__all__'

class ItemPotencialSerializer(ModelSerializer):
    class Meta:
        model = ItemPotencial
        fields = '__all__'