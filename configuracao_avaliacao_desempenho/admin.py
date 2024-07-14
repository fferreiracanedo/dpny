from django.contrib import admin
from .models import Competencia
from .models import Potencial


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ['id', 'competencia', 'tipo']

'''
@admin.register(Potencial)
class PotencialAdmin(admin.ModelAdmin):
    list_display = ['id', 'potencial']
'''