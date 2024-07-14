from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Endereco


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class EnderecoForm(forms.Form, forms.ModelForm):
    class Meta:
        model = Endereco
        fields = [
            'cep',
            'logradouro',
            'complemento',
            'numero',
            'bairro',
            'pais',
            'estado',
            'cidade',
        ]
