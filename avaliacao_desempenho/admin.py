from django.contrib import admin
from django_object_actions import DjangoObjectActions
from configuracao_avaliacao_desempenho.models import Meta
from .models import AvaliacaoDesempenho
from .models import GrupoAvaliacaoDesempenho
from .models import ItemCompetencia
from .models import ItemMeta
from .models import ItemPotencial


class MetaInline(admin.TabularInline):
    model = Meta
    extra = 0
    fields = ['meta', 'peso', 'explicativo', 'resultado_esperado', 'forma_medicao']

class ItemCompetenciaInline(admin.TabularInline):
    model = ItemCompetencia
    extra = 0

class ItemMetaInline(admin.TabularInline):
    model = ItemMeta
    extra = 0

class ItemPotencialInline(admin.TabularInline):
    model = ItemPotencial
    extra = 0

@admin.register(AvaliacaoDesempenho)
class AvaliacaoDesempenhoAdmin(admin.ModelAdmin):
    list_display = ['id', 'pessoa', 'avaliador', 'tipo_avaliacao', 'nota_competencias', 'nota_metas', 'nota_potencial']
    readonly_fields = ['data_criacao']
    fieldsets = (
        ('Dados Principais', {'fields': (
            'pessoa',
            'respondida',
            'avaliador',
            'data',
            'tipo_avaliacao',
            'resultado_comite',
            'comentario',
        )}),
        ('Avaliação', {'fields': (
            'resposta_potencial',
        )}),
    )
    list_filter = ('respondida', 'tipo_avaliacao', 'resposta_potencial', 'avaliador', 'pessoa')
    search_fields = ('pessoa__nome','avaliador__username')
    inlines = [ItemCompetenciaInline, ItemMetaInline]

@admin.register(GrupoAvaliacaoDesempenho)
class GrupoAvaliacaoDesempenhoAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ['id', 'nome', 'data_inicial', 'data_final']
    readonly_fields = ['data_criacao', 'ja_gerado']
    filter_horizontal = [
        'pessoa',
        'competencia',
    ]

    fieldsets = (
        ('Dados Principais', {'fields': (
            'nome',
            'data_inicial',
            'data_final',
            'descricao',
            'data_criacao',
            'ja_gerado',
        )}),
        ('Selecione os Participantes', {'fields': (
            'pessoa',
        )}),
        ('Configuração da Avaliação', {'fields': (
            'competencia',
        )}),
    )

    def gerar_avaliacoes(self, request, obj):
        obj.gerar_avaliacoes()

    gerar_avaliacoes.label = 'Gerar Avaliações'
    gerar_avaliacoes.short_description = 'Clique para gerar as avaliações de acordo com a configuração informada'

    change_actions = ('gerar_avaliacoes',)
