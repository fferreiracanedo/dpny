from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django_object_actions import DjangoObjectActions
from .models import Acao
from .models import Pdi
from .models import PdiCompetencia
from .models import PdiCurso
from .models import PdiEspecializacao
from .models import PdiFormacaoAcademica
from .models import PdiIdioma
from .models import PdiProfissional


class PdiCursoInline(admin.TabularInline):
    model = PdiCurso
    extra = 0


class PdiEspecializacaoInline(admin.TabularInline):
    model = PdiEspecializacao
    extra = 0


class PdiFormacaoAcademicaInline(admin.TabularInline):
    model = PdiFormacaoAcademica
    extra = 0


class PdiIdiomaInline(admin.TabularInline):
    model = PdiIdioma
    extra = 0


class PdiProfissionalInline(admin.TabularInline):
    model = PdiProfissional
    extra = 0


class PdiCompetenciaInline(admin.TabularInline):
    model = PdiCompetencia
    extra = 0


@admin.register(Pdi)
class PdiAdmin(DjangoObjectActions, admin.ModelAdmin):
    model = Pdi
    list_display = ('id','pessoa')
    search_fields = ('pessoa',)

    inlines = [PdiCompetenciaInline]
    '''
    def enviar_pdi(self, request, obj):
        obj.enviar_email()

    enviar_pdi.label = 'Enviar para Coach'
    enviar_pdi.short_description = 'Clique para enviar o PDI para o coach'

    change_actions = ('enviar_pdi',)
    '''

@admin.register(Acao)
class AcaoAdmin(ImportExportModelAdmin):
    model = Acao
    list_display = ('id','nome')
    search_fields = ('nome',)


#admin.site.register(Pdi, PdiAdmin)
#admin.site.register(Acao, AcaoAdmin)