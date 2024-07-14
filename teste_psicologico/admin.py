from django.contrib import admin
from .models import Afirmativa
from .models import Resposta
from .models import TemplateTestePsicologico
from .models import TestePsicologico


# Register your models here.
class RespostaInline(admin.TabularInline):
    model = Resposta
    readonly_fields = ('resposta', 'midia')
    exclude = ('afirmativa',)
    extra = 0


class AfirmativaInline(admin.TabularInline):
    model = Afirmativa
    extra = 0
    exclude = ('perfil','template_teste_psicologico')


class AfirmativaTemplateInline(admin.TabularInline):
    model = Afirmativa
    extra = 0
    exclude = ('perfil', 'teste_psicologico')


class AfirmativaAdmin(admin.ModelAdmin):
    model = Afirmativa
    list_display = ('id','afirmativa','ordem')
    search_fields = ('afirmativa',)
    exclude = ('template_teste_psicologico',)


class TemplateTestePsicologicoAdmin(admin.ModelAdmin):
    model = TemplateTestePsicologico,
    list_display = ('id', 'nome')
    inlines = [AfirmativaTemplateInline]


class TestePsicologicoAdmin(admin.ModelAdmin):
    model = TestePsicologico
    list_display = ('id','pessoa','perfil', 'aprovado_gestor', 'respondido', 'marcar_entrevista')
    list_filter = ['perfil', 'pessoa']

    inlines = [AfirmativaInline, RespostaInline]


#admin.site.register(Afirmativa, AfirmativaAdmin)
admin.site.register(TemplateTestePsicologico, TemplateTestePsicologicoAdmin)
admin.site.register(TestePsicologico, TestePsicologicoAdmin)