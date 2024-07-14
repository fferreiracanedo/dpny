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
from teste_psicologico.models import Resposta
from teste_psicologico.models import TestePsicologico

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


class RespostaSerializer(ModelSerializer):
    midia = Base64ImageField(max_length=None, use_url=True, required=False)
    
    class Meta:
        model = Resposta
        fields = '__all__'
    
    def create(self, validated_data):
        validated_data['teste_psicologico'].respondido = True
        validated_data['teste_psicologico'].save()

        obj = Resposta.objects.create(**validated_data)

        return obj


class TestePsicologicoSerializer(ModelSerializer):
    class Meta:
        model = TestePsicologico
        fields = '__all__'
