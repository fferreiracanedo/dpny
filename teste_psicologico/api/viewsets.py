from django.db.models import Count
from rest_framework.decorators import action

__author__ = "Edson de Lima Cosme Junior"
__copyright__ = "Copyright 2019, Edson Junior"
__credits__ = ["Outbox Sistemas"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Edson de Lima Cosme Junior"
__email__ = "edson.junior@outboxsistemas.com"
__status__ = "Production"

from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import RespostaSerializer
from .serializers import TestePsicologicoSerializer

from teste_psicologico.models import Resposta
from teste_psicologico.models import TestePsicologico


class RespostaViewSet(ModelViewSet):
    serializer_class = RespostaSerializer
    queryset = Resposta.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('teste_psicologico',)


class TestePsicologicoViewSet(ModelViewSet):
    serializer_class = TestePsicologicoSerializer
    queryset = TestePsicologico.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('pessoa','perfil')