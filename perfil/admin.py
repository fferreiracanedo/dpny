from django.contrib import admin
from django_object_actions import DjangoObjectActions
from .models import Perfil
from .models import AnaliseTalento
from .models import ConfigAnaliseTalento
from dashboard.views import ranking
from teste_psicologico.models import Afirmativa


class AfirmativaInline(admin.TabularInline):
    model = Afirmativa
    extra = 0
    exclude = ('template_teste_psicologico', 'teste_psicologico')


class AnaliseTalentoInline(admin.TabularInline):
    model = AnaliseTalento
    extra = 0
    readonly_fields = ('nota_experiencia','nota_formacao_academica','nota_curso','nota_idioma',
        'nota_requisitos_tecnicos','nota_total')


class AnaliseTalentoAdmin(admin.ModelAdmin):
    model = AnaliseTalento
    list_display = ('id','perfil','pessoa','nota_experiencia', 'nota_formacao_academica', 'nota_curso', 
        'nota_idioma', 'nota_requisitos_tecnicos', 'nota_total')
    readonly_fields = ('nota_experiencia', 'nota_formacao_academica', 'nota_curso', 'nota_idioma', 
        'nota_requisitos_tecnicos', 'nota_total')
    list_filter = ('perfil',)


class PerfilAdmin(DjangoObjectActions, admin.ModelAdmin):
    model = Perfil
    list_display = ('id','nome','cargo',)
    search_fields = ('nome','cargo__titulo',)
    list_filter = ('cargo',)

    fieldsets = (
        ('Dados do Perfil', {'fields':(
            'nome',
            'cargo',
            'gestor',
            'visualizar_site',
            'visualizar_linkedin',
            'visualizar_funcionarios',
            'data_abertura',
            'status',
            'beneficios'
        )}),
        ('Critérios de Avaliação', {'fields': (
            'nota_maxima_requisitos_tecnicos',
            'nota_maxima_experiencia',
            'nota_maxima_formacao_academica',
            'nivel_escolaridade_exigido',
            'nota_maxima_cursos',
            'nota_maxima_idiomas',
        )}),
        ('Pesos de Avaliação', {'fields': (
            'peso_requisitos_tecnicos',
            'peso_experiencia',
            'peso_formacao_academica',
            'peso_cursos',
            'peso_idiomas',
            'template_teste_psicologico'
        )}),
    )

    inlines = [AfirmativaInline, AnaliseTalentoInline]

    def gerar_testes(self, request, obj):
        obj.gerar_testes()
    
    gerar_testes.label = 'Gerar Testes'
    gerar_testes.short_description = 'Clique para gerar os testes para os 3 primeiros do ranking'

    def dashboard_ranking(self, request, obj):
        return ranking(request, obj.id)

    dashboard_ranking.label = 'Ranking'
    dashboard_ranking.short_description = 'Clique para visualizar o ranking'

    change_actions = ('dashboard_ranking', 'gerar_testes')


@admin.register(ConfigAnaliseTalento)
class ConfigAnaliseTalentoAdmin(admin.ModelAdmin):
    list_display = ('id','nome','maximo_analises','quantidade_atual_analises')


admin.site.register(Perfil,PerfilAdmin)
admin.site.register(AnaliseTalento,AnaliseTalentoAdmin)