from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Pessoa
from .models import ExperienciaProfissional
from .models import Filho
from .models import FormacaoAcademica
from .models import Curso
from .models import Projeto
from .models import RequisitoTecnico
from .models import Midia
from .forms import PessoaForm
from formacao.models import Idioma


class ExperienciaProfissionalInline(admin.TabularInline):
    model = ExperienciaProfissional
    extra = 0
    fields = ['empresa', 'cargo', 'data_inicio', 'data_termino', 'trabalho_atual']

    class Media:
        js = ("js/hide_addlink.js",)


class FilhoInline(admin.TabularInline):
    model = Filho
    extra = 0


class FormacaoAcademicaInline(admin.TabularInline):
    model = FormacaoAcademica
    extra = 0


class CursoInline(admin.TabularInline):
    model = Curso
    extra = 0


class IdiomaInline(admin.TabularInline):
    model = Idioma
    extra = 0


class ProjetoInline(admin.TabularInline):
    model = Projeto
    extra = 0


class MidiaInline(admin.TabularInline):
    model = Midia
    extra = 0


@admin.register(RequisitoTecnico)
class RequisitoTecnicoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']

@admin.register(ExperienciaProfissional)
class ExperienciaProfissional(ImportExportModelAdmin):
    model = ExperienciaProfissional
    list_display = ("id", "cargo")

    class Media:
        js = ("js/hide_addlink.js",)

@admin.register(FormacaoAcademica)
class ExperienciaProfissional(ImportExportModelAdmin):
    model = FormacaoAcademica
    list_display = ("id", "curso")

    class Media:
        js = ("js/hide_addlink.js",)

class PessoaAdmin(ImportExportModelAdmin):
    model = Pessoa
    #form = PessoaForm
    list_display = ('id','nome','user','gestor','tempo_empresa','is_lider')
    search_fields = ('nome',)
    filter_horizontal = ['requisitos_tecnicos', 'pares_avaliadores']
    #readonly_fields = ('user',)
    '''
    fieldsets = (
        ('Dados Pessoais', {'fields': (
            'nome',
            'gestor',
            'cargo',
            'user',
            'grupo',
            'filial',
            'matricula',
            'chave_integracao'
        )}),
    )
    '''
    fieldsets = (
        ('Dados Pessoais', {'fields': (
            'nome',
            'data_nascimento',
            'estado_civil',
            'nacionalidade',
            'municipio_nascimento',
            'cor',
            'sexo',
            'foto',
            'nascimento_anexo',
            'casamento_anexo',
            'divorcio_anexo',
        )}),
        ('Documentos - CPF', {'fields': (
            'cpf', 
            'cpf_anexo',
        )}),
        ('Documentos - RG', {'fields': (
            'rg', 
            'rg_orgao_expedidor', 
            'rg_data_expedicao', 
            'rg_anexo',
        )}),
        ('Documentos - CTPS', {'fields': (
            'pis_numero',
            'pis_anexo', 
            'ctps_numero', 
            'ctps_serie', 
            'ctps_data_expedicao', 
            'ctps_uf', 
            'ctps_anexo',
        )}),
        ('Documentos - Título de Eleitor', {'fields': (
            'titulo_eleitor', 
            'titulo_eleitor_zona', 
            'titulo_eleitor_secao', 
            'titulo_eleitor_anexo',
        )}),
        ('Documentos - Habilitação', {'fields': (
            'habilitacao_numero', 
            'habilitacao_categoria',
        )}),
        ('Contatos', {'fields': (
            'email',
            'celular',
            'telefone',
        )}),
        ('Endereço', {'fields': (
            'logradouro',
            'numero_endereco',
            'complemento',
            'bairro',
            'cep',
            'cidade',
            'estado',
        )}),
        ('Dados Profissionais', {'fields': (
            'pretensao_salarial',
            'disponibilidade_viajar',
            'ja_trabalhou',
            'quando_trabalhou',
            'projeto_trabalhou',
            'link_perfil_linkedin',
            'curriculo',
            'cargo',
            'data_contratacao',
            'gestor',
            'pares_avaliadores'
        )}),
        ('Histórico Profissional', {'fields': (
            'atividades_relevantes1',
            'atividades_relevantes2',
            'atividades_relevantes3',
            'atividades_relevantes4',
            'atividades_relevantes5',
            'medicao_quantitativa_atividades_relevantes1',
            'medicao_quantitativa_atividades_relevantes2',
            'medicao_quantitativa_atividades_relevantes3',
            'medicao_quantitativa_atividades_relevantes4',
            'medicao_quantitativa_atividades_relevantes5',
            'medicao_qualitativa_atividades_relevantes1',
            'medicao_qualitativa_atividades_relevantes2',
            'medicao_qualitativa_atividades_relevantes3',
            'medicao_qualitativa_atividades_relevantes4',
            'medicao_qualitativa_atividades_relevantes5',
        )}),
        ('Requisitos Técnicos', {'fields': (
            'requisitos_tecnicos',
        )}),
        ('Parentesco', {'fields': (
            'nome_mae',
            'nome_pai'
        )}),
        ('Outros Dados', {'fields': (
            'user',
            'aceite_politica_privacidade'
        )}),
    )
    

    inlines = [ExperienciaProfissionalInline,FormacaoAcademicaInline,CursoInline, IdiomaInline, MidiaInline, FilhoInline]

    class Media:
        js = ("js/hide_addlink.js",)


admin.site.register(Pessoa, PessoaAdmin)