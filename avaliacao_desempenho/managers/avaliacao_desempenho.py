from django.db import models
from django.db.models import Avg
from collections import namedtuple


class AvaliacaoDesempenhoManager(models.Manager):
    def media_competencias(self, pessoa, tipo):
        queryset = self.filter(
            pessoa=pessoa,
            respondida=True, 
            tipo_avaliacao=tipo
        )

        soma_competencias = 0
        for avaliacao in queryset:
            soma_competencias += avaliacao.nota_competencias if avaliacao.nota_competencias else 0
        
        try:
            return round(soma_competencias / len(queryset), 2)
        except:
            return None
    
    def resultado_avaliacao_faixa_etaria(self):
        queryset = self.filter(respondida=True)

        resultado_final = [
            self.resultado_faixa_etaria("Não informado", 0, 0, queryset),
            self.resultado_faixa_etaria("Até 20 anos", 0, 20, queryset),
            self.resultado_faixa_etaria("Entre 21 e 25 anos", 21, 25, queryset),
            self.resultado_faixa_etaria("Entre 26 e 30 anos", 26, 30, queryset),
            self.resultado_faixa_etaria("Entre 31 e 35 anos", 31, 35, queryset),
            self.resultado_faixa_etaria("Entre 36 e 40 anos", 36, 40, queryset),
            self.resultado_faixa_etaria("Entre 41 e 45 anos", 41, 45, queryset),
            self.resultado_faixa_etaria("Entre 46 e 50 anos", 46, 50, queryset),
            self.resultado_faixa_etaria("Entre 51 e 55 anos", 51, 55, queryset),
            self.resultado_faixa_etaria("Entre 56 e 60 anos", 56, 60, queryset),
            self.resultado_faixa_etaria("Acima de 60 anos", 60, 999, queryset)
        ]

        return resultado_final
    
    def resultado_faixa_etaria(self, faixa_etaria, idade_minima, idade_maxima, queryset):
        Resultado = namedtuple('Resultado', 'faixa_etaria total media maior_nota menor_nota')
        
        quantidade_respondida = 0
        maior_nota = 0
        menor_nota = 100
        melhor_avaliacao = None
        pior_avaliacao = None
        total_notas = 0
        media_geral = 0

        for avaliacao in queryset:
            if avaliacao.pessoa.idade:
                if avaliacao.pessoa.idade >= idade_minima and avaliacao.pessoa.idade <= idade_maxima:
                    total_notas += avaliacao.nota_competencias if avaliacao.nota_competencias else 0
                    quantidade_respondida += 1

                    if avaliacao.nota_competencias:
                        if avaliacao.nota_competencias > maior_nota:
                            melhor_avaliacao = avaliacao
                            maior_nota = avaliacao.nota_competencias
                        
                        if avaliacao.nota_competencias < menor_nota:
                            pior_avaliacao = avaliacao
                            menor_nota = avaliacao.nota_competencias
            else:
                if idade_minima == 0 and idade_maxima == 0:
                    total_notas += avaliacao.nota_competencias if avaliacao.nota_competencias else 0
                    quantidade_respondida += 1

                    if avaliacao.nota_competencias:
                        if avaliacao.nota_competencias > maior_nota:
                            melhor_avaliacao = avaliacao
                            maior_nota = avaliacao.nota_competencias
                        
                        if avaliacao.nota_competencias < menor_nota:
                            pior_avaliacao = avaliacao
                            menor_nota = avaliacao.nota_competencias

        media_geral = total_notas/quantidade_respondida if quantidade_respondida > 0 else 0

        return Resultado(
            faixa_etaria,
            quantidade_respondida,
            media_geral,
            melhor_avaliacao,
            pior_avaliacao
        )
    
    def resultado_liderados(self, pessoa):
        Resultado = namedtuple('Resultado', 'pessoa total media maior_nota menor_nota')
        
        quantidade_respondida = 0
        maior_nota = 0
        menor_nota = 100
        melhor_avaliacao = None
        pior_avaliacao = None
        total_notas = 0
        media_geral = 0

        queryset = self.filter(respondida=True, pessoa=pessoa, tipo_avaliacao='par')

        for avaliacao in queryset:
            total_notas += avaliacao.nota_competencias
            quantidade_respondida += 1

            if avaliacao.nota_competencias > maior_nota:
                melhor_avaliacao = avaliacao
                maior_nota = avaliacao.nota_competencias
            
            if avaliacao.nota_competencias < menor_nota:
                pior_avaliacao = avaliacao
                menor_nota = avaliacao.nota_competencias

        media_geral = total_notas/quantidade_respondida if quantidade_respondida > 0 else 0

        return Resultado(
            pessoa.nome,
            quantidade_respondida,
            media_geral,
            melhor_avaliacao,
            pior_avaliacao
        )

