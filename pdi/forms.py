from django import forms
from django.forms import ModelForm
from .models import Pdi
from .models import PdiCompetencia
from configuracao_avaliacao_desempenho.models import Competencia


class PdiForm(forms.Form, forms.ModelForm):
    class Meta:
        model = Pdi
        fields = '__all__'

        widgets = {
            'pessoa': forms.HiddenInput(),
        }


class PdiCompetenciaForm(forms.Form, forms.ModelForm):
    class Meta:
        model = PdiCompetencia
        fields = ('competencia', 'acao', 'pdi')


PdiCompetenciaInlineFormSet = forms.inlineformset_factory(
    Pdi,
    PdiCompetencia,
    extra=1,
    form=PdiCompetenciaForm
)