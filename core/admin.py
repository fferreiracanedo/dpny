from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Cidade
from .models import Endereco
from .models import Estado
from .models import Filial
from .models import Grupo
from .models import Pais
from .models import EstadoCivil


class EnderecoInline(admin.StackedInline):
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
    exclude = ['data_criacao']
    list_select_related = (
        'pais',
        'estado',
        'cidade',
    )


@admin.register(Cidade)
class CidadeAdmin(ImportExportModelAdmin):
    list_display = ['id', 'nome', 'estado', 'pais']
    list_filter = ['estado', 'estado__pais']
    readonly_fields = ['data_criacao']


@admin.register(Estado)
class EstadoAdmin(ImportExportModelAdmin):
    list_display = ['id', 'nome', 'codigo']
    list_filter = ['pais']
    readonly_fields = ['data_criacao']


@admin.register(Filial)
class FilialAdmin(ImportExportModelAdmin):
    list_display = ['id', 'nome']
    readonly_fields = ['data_criacao']


@admin.register(Grupo)
class GrupoAdmin(ImportExportModelAdmin):
    list_display = ['id', 'nome']
    readonly_fields = ['data_criacao']


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    readonly_fields = ['data_criacao']


@admin.register(EstadoCivil)
class EstadoCivilAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    readonly_fields = ['data_criacao']
