from django.forms import ModelForm
from .models import TestePsicologico


class TestePsicologicoForm(ModelForm):
    class Meta:
        model = TestePsicologico
        fields = '__all__'
