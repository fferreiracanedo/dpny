from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Pessoa
from .models import ExperienciaProfissional
from .models import FormacaoAcademica
from .models import Curso
from formacao.models import Idioma


class DateInput(forms.DateInput):
    input_type = 'date'


class PessoaForm(forms.Form, forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=DateInput(
            format='%Y-%m-%d'
        ),
        input_formats=('%Y-%m-%d',),
        help_text="Campo Obrigatório*"
    )

    quando_trabalhou = forms.DateField(
        widget=DateInput(
            format='%Y-%m-%d'
        ),
        input_formats=('%Y-%m-%d',),
        required=False
    )

    class Meta:
        model = Pessoa
        fields = '__all__'
        widgets = {
            'data_nascimento': DateInput(
                attrs={
                    'type': 'date',
                    'format': '%Y-%m-%d'
                }
            ),
            'quando_trabalhou': DateInput(
                attrs={
                    'type': 'date',
                    'format': '%Y-%m-%d'
                }
            ),
        }


class ExperienciaProfissionalForm(ModelForm):
    data_inicio = forms.DateField(
        widget=DateInput(
            format='%Y-%m-%d'
        ),
        input_formats=('%Y-%m-%d',)
    )

    data_termino = forms.DateField(
        widget=DateInput(
            format='%Y-%m-%d'
        ),
        input_formats=('%Y-%m-%d',)
    )
    
    class Meta:
        model = ExperienciaProfissional
        fields = '__all__'


class FormacaoAcademicaForm(ModelForm):
    data_inicio = forms.DateField(
        widget=DateInput(
            format='%Y-%m-%d'
        ),
        input_formats=('%Y-%m-%d',)
    )

    data_termino = forms.DateField(
        widget=DateInput(
            format='%Y-%m-%d'
        ),
        input_formats=('%Y-%m-%d',)
    )

    class Meta:
        model = FormacaoAcademica
        fields = '__all__'


class CursoForm(ModelForm):
    data_inicio = forms.DateField(
        widget=DateInput(
            format='%Y-%m-%d'
        ),
        input_formats=('%Y-%m-%d',)
    )

    data_termino = forms.DateField(
        widget=DateInput(
            format='%Y-%m-%d'
        ),
        input_formats=('%Y-%m-%d',)
    )

    class Meta:
        model = Curso
        fields = '__all__'


class IdiomaForm(ModelForm):
    class Meta:
        model = Idioma
        fields = '__all__'


ExperienciaProfissionalInlineFormSet = inlineformset_factory(
    Pessoa, ExperienciaProfissional, extra=0, min_num=1,
    form=ExperienciaProfissionalForm
)


FormacaoAcademicaInlineFormSet = inlineformset_factory(
    Pessoa, FormacaoAcademica, extra=0, min_num=1,
    form=FormacaoAcademicaForm
)


CursoInlineFormSet = inlineformset_factory(
    Pessoa, Curso, extra=0, min_num=1,
    form=CursoForm
)


IdiomaInlineFormSet = inlineformset_factory(
    Pessoa, Idioma, extra=0, min_num=1,
    form=IdiomaForm
)