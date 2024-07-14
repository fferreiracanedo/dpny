from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import AnoFormacao
from .models import CargaHoraria
from .models import Especializacao
from .models import FormacaoAcademica
from .models import Idioma
from .models import Instituicao
from .models import Curso


class AnoFormacaoAdmin(ImportExportModelAdmin):
    model = AnoFormacao
    list_display = ('id','ano')
    search_fields = ('ano',)


class CargaHorariaAdmin(ImportExportModelAdmin):
    model = CargaHoraria
    list_display = ('id','horas','pontos')
    search_fields = ('horas',)


class EspecializacaoAdmin(ImportExportModelAdmin):
    model = Especializacao
    list_display = ('id','titulo','pontos')
    search_fields = ('pontos',)


class FormacaoAcademicaAdmin(ImportExportModelAdmin):
    model = FormacaoAcademica
    list_display = ('id','titulo','pontos')
    search_fields = ('titulo',)


class IdiomaAdmin(ImportExportModelAdmin):
    model = Idioma
    list_display = ('id','titulo','pontos','nivel')
    search_fields = ('titulo',)
    list_filter = ('nivel',)


class InstituicaoAdmin(ImportExportModelAdmin):
    model = Instituicao
    list_display = ('id','nome')
    search_fields = ('nome',)


class CursoAdmin(ImportExportModelAdmin):
    model = Curso
    list_display = ('id','titulo')
    search_fields = ('titulo',)


#admin.site.register(AnoFormacao, AnoFormacaoAdmin)
#admin.site.register(CargaHoraria, CargaHorariaAdmin)
#admin.site.register(Especializacao, EspecializacaoAdmin)
#admin.site.register(FormacaoAcademica, FormacaoAcademicaAdmin)
#admin.site.register(Idioma, IdiomaAdmin)
#admin.site.register(Instituicao, InstituicaoAdmin)
admin.site.register(Curso,CursoAdmin)