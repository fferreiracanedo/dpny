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

from .serializers import PessoaSerializer
from .serializers import ExperienciaProfissionalSerializer
from .serializers import FilhoSerializer
from .serializers import FormacaoAcademicaSerializer
from .serializers import CursoSerializer
from .serializers import IdiomaSerializer
from .serializers import MidiaSerializer

from pessoa.models import Pessoa
from pessoa.models import ExperienciaProfissional
from pessoa.models import Filho
from pessoa.models import FormacaoAcademica
from pessoa.models import Curso
from pessoa.models import Midia
from formacao.models import Idioma


class PessoaViewSet(ModelViewSet):
    serializer_class = PessoaSerializer
    queryset = Pessoa.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user',)

    @action(methods=['delete'], detail=True)
    def cpf_anexo(self, request, pk):
        queryset = Pessoa.objects.all()
        pessoa = get_object_or_404(queryset, id=pk)

        pessoa.cpf_anexo = None

        pessoa.save()

        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data)

    @action(methods=['delete'], detail=True)
    def pis_anexo(self, request, pk):
        queryset = Pessoa.objects.all()
        pessoa = get_object_or_404(queryset, id=pk)

        pessoa.pis_anexo = None

        pessoa.save()

        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data)

    @action(methods=['delete'], detail=True)
    def rg_anexo(self, request, pk):
        queryset = Pessoa.objects.all()
        pessoa = get_object_or_404(queryset, id=pk)

        pessoa.rg_anexo = None

        pessoa.save()

        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data)

    @action(methods=['delete'], detail=True)
    def titulo_eleitor_anexo(self, request, pk):
        queryset = Pessoa.objects.all()
        pessoa = get_object_or_404(queryset, id=pk)

        pessoa.titulo_eleitor_anexo = None

        pessoa.save()

        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data)

    @action(methods=['delete'], detail=True)
    def ctps_anexo(self, request, pk):
        queryset = Pessoa.objects.all()
        pessoa = get_object_or_404(queryset, id=pk)

        pessoa.ctps_anexo = None

        pessoa.save()

        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data)

    @action(methods=['delete'], detail=True)
    def curriculo_anexo(self, request, pk):
        queryset = Pessoa.objects.all()
        pessoa = get_object_or_404(queryset, id=pk)

        pessoa.curriculo_anexo = None

        pessoa.save()

        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data)

    @action(methods=['delete'], detail=True)
    def foto(self, request, pk):
        queryset = Pessoa.objects.all()
        pessoa = get_object_or_404(queryset, id=pk)

        pessoa.foto = None

        pessoa.save()

        serializer = PessoaSerializer(pessoa)
        return Response(serializer.data)


class ExperienciaProfissionalViewSet(ModelViewSet):
    serializer_class = ExperienciaProfissionalSerializer
    queryset = ExperienciaProfissional.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('pessoa',)


class FilhoViewSet(ModelViewSet):
    serializer_class = FilhoSerializer
    queryset = Filho.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('pessoa',)


class FormacaoAcademicaViewSet(ModelViewSet):
    serializer_class = FormacaoAcademicaSerializer
    queryset = FormacaoAcademica.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('pessoa',)

    @action(methods=['delete'], detail=True)
    def certificado(self, request, pk):
        queryset = FormacaoAcademica.objects.all()
        formacao_academica = get_object_or_404(queryset, id=pk)

        formacao_academica.certificado = None

        formacao_academica.save()

        serializer = FormacaoAcademicaSerializer(formacao_academica)
        return Response(serializer.data)


class CursoViewSet(ModelViewSet):
    serializer_class = CursoSerializer
    queryset = Curso.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('pessoa',)

    @action(methods=['delete'], detail=True)
    def certificado(self, request, pk):
        queryset = Curso.objects.all()
        curso = get_object_or_404(queryset, id=pk)

        curso.certificado = None

        curso.save()

        serializer = CursoSerializer(curso)
        return Response(serializer.data)


class IdiomaViewSet(ModelViewSet):
    serializer_class = IdiomaSerializer
    queryset = Idioma.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('pessoa',)

    @action(methods=['delete'], detail=True)
    def certificado(self, request, pk):
        queryset = Idioma.objects.all()
        idioma = get_object_or_404(queryset, id=pk)

        idioma.certificado = None

        idioma.save()

        serializer = IdiomaSerializer(idioma)
        return Response(serializer.data)


class MidiaViewSet(ModelViewSet):
    serializer_class = MidiaSerializer
    queryset = Midia.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('pessoa',)
