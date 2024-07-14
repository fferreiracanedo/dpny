__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2019, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from django.db.models import Count
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import AvaliacaoDesempenhoSerializer
from .serializers import ItemCompetenciaSerializer
from .serializers import ItemMetaSerializer
from .serializers import ItemPotencialSerializer

from avaliacao_desempenho.models import AvaliacaoDesempenho
from avaliacao_desempenho.models import ItemCompetencia
from avaliacao_desempenho.models import ItemMeta
from avaliacao_desempenho.models import ItemPotencial


class AvaliacaoDesempenhoViewSet(ModelViewSet):
    serializer_class = AvaliacaoDesempenhoSerializer
    queryset = AvaliacaoDesempenho.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('avaliador', 'pessoa')


class ItemCompetenciaViewSet(ModelViewSet):
    serializer_class = ItemCompetenciaSerializer
    queryset = ItemCompetencia.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('avaliacao_desempenho',)


class ItemMetaViewSet(ModelViewSet):
    serializer_class = ItemMetaSerializer
    queryset = ItemMeta.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('avaliacao_desempenho',)


class ItemPotencialViewSet(ModelViewSet):
    serializer_class = ItemPotencialSerializer
    queryset = ItemPotencial.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('avaliacao_desempenho',)