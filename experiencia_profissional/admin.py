from django.contrib import admin
from .models import Cargo
from .forms import CargoForm
from .models import Experiencia
from .models import AreaAtuacao
from import_export.admin import ImportExportModelAdmin


class CargoAdmin(ImportExportModelAdmin):
    model = Cargo
    form = CargoForm
    list_display = ('id', 'titulo', 'area_atuacao')
    search_fields = ('titulo',)
    filter_horizontal = ('requisitos_tecnicos',)

    fieldsets = (
        ('Dados do Perfil', {'fields': (
            'titulo',
            'codigo',
            'atividades',
            'responsabilidades',
            'missao',
            'observacoes',
            'area_atuacao',
            'requisitos_tecnicos',
        )}),
    )


class ExperienciaAdmin(ImportExportModelAdmin):
    model = Experiencia
    list_display = ('id','experiencia','pontos')
    search_fields = ('experiencia',)


class AreaAtuacaoAdmin(ImportExportModelAdmin):
    model = AreaAtuacao
    list_display = ('id','nome')
    search_fields = ('nome',)


admin.site.register(Cargo, CargoAdmin)
#admin.site.register(Experiencia, ExperienciaAdmin)
admin.site.register(AreaAtuacao, AreaAtuacaoAdmin)