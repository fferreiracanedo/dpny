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
from pessoa.models import Pessoa
from pessoa.models import ExperienciaProfissional
from pessoa.models import Filho
from pessoa.models import FormacaoAcademica
from pessoa.models import Curso
from pessoa.models import Midia
from formacao.models import Idioma


class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')

            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (file_name, file_extension, )
            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


class Base64FileField(serializers.FileField):

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')

            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_file')

            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            file_extension = self.get_file_extension(header)
            complete_file_name = "%s.%s" % (file_name, file_extension, )
            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64FileField, self).to_internal_value(data)

    def get_file_extension(self, header):
        extension, content = header.split('-data:')

        return extension


class PessoaSerializer(ModelSerializer):
    cpf_anexo = Base64FileField(max_length=None, use_url=True, required=False)
    pis_anexo = Base64FileField(max_length=None, use_url=True, required=False)
    rg_anexo = Base64FileField(max_length=None, use_url=True, required=False)
    titulo_eleitor_anexo = Base64FileField(max_length=None, use_url=True, required=False)
    ctps_anexo = Base64FileField(max_length=None, use_url=True, required=False)
    curriculo = Base64FileField(max_length=None, use_url=True, required=False)
    foto = Base64ImageField(max_length=None, use_url=True, required=False)
    video = Base64FileField(max_length=None, use_url=True, required=False)
    nascimento_anexo = Base64FileField(max_length=None, use_url=True, required=False)
    casamento_anexo = Base64FileField(max_length=None, use_url=True, required=False)
    divorcio_anexo = Base64FileField(max_length=None, use_url=True, required=False)
    habilitacao_anexo = Base64FileField(max_length=None, use_url=True, required=False)
    residencia_anexo = Base64FileField(max_length=None, use_url=True, required=False)

    class Meta:
        model = Pessoa
        fields = '__all__'
        exclude_fields = ('user', 'cargo', 'pares_avaliadores')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        del validated_data['requisitos_tecnicos']
        del validated_data['pares_avaliadores']

        obj = Pessoa.objects.create(**validated_data)

        return obj


class ExperienciaProfissionalSerializer(ModelSerializer):
    class Meta:
        model = ExperienciaProfissional
        fields = (
            'id', 'empresa', 'cargo', 'outro_cargo', 'data_inicio', 'data_termino', 'cargo_atual', 'tempo', 'trabalho_atual'
        )
    
    def create(self, validated_data):
        pessoa = Pessoa.objects.filter(user=self.context['request'].user.id).first()    
        validated_data['pessoa'] = pessoa
        obj = ExperienciaProfissional.objects.create(**validated_data)

        return obj


class FilhoSerializer(ModelSerializer):
    cpf_anexo = Base64ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = Filho
        fields = (
            'id', 'nome', 'cpf', 'cpf_anexo', 'data_nascimento'
        )
    
    def create(self, validated_data):
        pessoa = Pessoa.objects.filter(user=self.context['request'].user.id).first()    
        validated_data['pessoa'] = pessoa
        obj = Filho.objects.create(**validated_data)

        return obj


class FormacaoAcademicaSerializer(ModelSerializer):
    certificado = Base64ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = FormacaoAcademica
        fields = (
            'id', 'nivel_escolaridade', 'curso', 'outro_curso', 'instituicao', 'situacao', 
            'data_inicio', 'data_termino', 'certificado'
        )
    
    def create(self, validated_data):
        pessoa = Pessoa.objects.filter(user=self.context['request'].user.id).first()    
        validated_data['pessoa'] = pessoa
        obj = FormacaoAcademica.objects.create(**validated_data)

        return obj


class CursoSerializer(ModelSerializer):
    certificado = Base64ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = Curso
        fields = (
            'id', 'curso', 'instituicao', 'carga_horaria',
            'data_inicio', 'data_termino', 'certificado'
        )
    
    def create(self, validated_data):
        pessoa = Pessoa.objects.filter(user=self.context['request'].user.id).first()    
        validated_data['pessoa'] = pessoa
        obj = Curso.objects.create(**validated_data)

        return obj


class IdiomaSerializer(ModelSerializer):
    certificado = Base64ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = Idioma
        fields = (
            'id', 'idioma', 'nivel', 'certificado'
        )
    
    def create(self, validated_data):
        pessoa = Pessoa.objects.filter(user=self.context['request'].user.id).first()    
        validated_data['pessoa'] = pessoa
        obj = Idioma.objects.create(**validated_data)

        return obj


class MidiaSerializer(ModelSerializer):
    arquivo = Base64ImageField(max_length=None, use_url=True, required=False)

    class Meta:
        model = Midia
        fields = (
            'id', 'titulo', 'descricao', 'link', 'arquivo', 'data_criacao'
        )
    
    def create(self, validated_data):
        pessoa = Pessoa.objects.filter(user=self.context['request'].user.id).first()    
        validated_data['pessoa'] = pessoa
        obj = Midia.objects.create(**validated_data)

        return obj
