from collections import namedtuple
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.db.models import Avg, Count
from datetime import date, datetime, timedelta
from pessoa.models import Pessoa
from perfil.models import Perfil
from perfil.models import AnaliseTalento
from pdi.models import Pdi
from teste_psicologico.models import TestePsicologico
from perfil.models import ConfigAnaliseTalento
from formacao.models import Especializacao
from formacao.models import FormacaoAcademica
from formacao.models import Instituicao
from formacao.models import Curso
from formacao.models import Idioma
from experiencia_profissional.models import Cargo
from experiencia_profissional.models import AreaAtuacao
from avaliacao_desempenho.models import AvaliacaoDesempenho, ItemCompetencia
from configuracao_avaliacao_desempenho.models import Competencia


# Create your views here.
@staff_member_required
def home(request):
    usuarios = User.objects.all().count()
    pessoas = Pessoa.objects.all().count()
    perfis = Perfil.objects.all().count()
    analises = AnaliseTalento.objects.all().count()
    testes = TestePsicologico.objects.all().count()

    formacoes = FormacaoAcademica.objects.all().count()
    instituicoes = Instituicao.objects.all().count()
    cursos = Curso.objects.all().count()
    cargos = Cargo.objects.all().count()
    areas_atuacao = AreaAtuacao.objects.all().count()

    return render(request, 'dashboard_home.html',
                  {
                      'usuarios': usuarios,
                      'pessoas': pessoas,
                      'perfis': perfis,
                      'analises': analises,
                      'testes': testes,
                      'formacoes': formacoes,
                      'instituicoes': instituicoes,
                      'cursos': cursos,
                      'cargos': cargos,
                      'areas_atuacao': areas_atuacao
                  })


@staff_member_required
def ranking(request, perfil):
    perfil = Perfil.objects.get(id=perfil)

    Ranking = namedtuple('Ranking', 'id pessoa id_pessoa foto pontuacao')

    # Ranking Final
    ranking_final = sorted([
        Ranking(
            analise.id,
            analise.pessoa.nome,
            analise.pessoa.id,
            analise.pessoa.foto,
            analise.nota_total.split()[-1][:-1] or 0
        ) for analise in perfil.analisetalento_set.all()
    ], key=lambda x: float(x.pontuacao), reverse=True)

    # Ranking Requisitos Técnicos
    ranking_requisitos_tecnicos = sorted([
        Ranking(
            analise.id,
            analise.pessoa.nome,
            analise.pessoa.id,
            analise.pessoa.foto,
            analise.nota_requisitos_tecnicos.split()[-1][:-1] or 0
        ) for analise in perfil.analisetalento_set.all()
    ], key=lambda x: float(x.pontuacao), reverse=True)

    # Ranking Experiência
    ranking_experiencia = sorted([
        Ranking(
            analise.id,
            analise.pessoa.nome,
            analise.pessoa.id,
            analise.pessoa.foto,
            analise.nota_experiencia.split()[-1][:-1] or 0
        ) for analise in perfil.analisetalento_set.all()
    ], key=lambda x: float(x.pontuacao), reverse=True)

    # Ranking Formação Acadêmica
    ranking_formacao_academica = sorted([
        Ranking(
            analise.id,
            analise.pessoa.nome,
            analise.pessoa.id,
            analise.pessoa.foto,
            analise.nota_formacao_academica.split()[-1][:-1] or 0
        ) for analise in perfil.analisetalento_set.all()
    ], key=lambda x: float(x.pontuacao), reverse=True)

    # Ranking Cursos
    ranking_curso = sorted([
        Ranking(
            analise.id,
            analise.pessoa.nome,
            analise.pessoa.id,
            analise.pessoa.foto,
            analise.nota_curso.split()[-1][:-1] or 0
        ) for analise in perfil.analisetalento_set.all()
    ], key=lambda x: float(x.pontuacao), reverse=True)

    # Ranking Idiomas
    ranking_idioma = sorted([
        Ranking(
            analise.id,
            analise.pessoa.nome,
            analise.pessoa.id,
            analise.pessoa.foto,
            analise.nota_idioma.split()[-1][:-1] or 0
        ) for analise in perfil.analisetalento_set.all()
    ], key=lambda x: float(x.pontuacao), reverse=True)

    return render(request, 'dashboard/ranking.html',
                  {
                      'perfil': perfil,
                      'ranking_final': ranking_final,
                      'ranking_requisitos_tecnicos': ranking_requisitos_tecnicos,
                      'ranking_experiencia': ranking_experiencia,
                      'ranking_formacao_academica': ranking_formacao_academica,
                      'ranking_curso': ranking_curso,
                      'ranking_idioma': ranking_idioma,
                      'esconder_sidebar': True
                  })


@staff_member_required
def analise(request, analise):
    analise = AnaliseTalento.objects.get(id=analise)

    return render(request, 'analise.html',
                  {
                      'analise': analise,
                      'nota_final': analise.nota_total.split()[-1][:-1] or 0,
                      'nota_essencia_talento': analise.nota_essencia_talento.split()[-1][:-1] or 0,
                      'nota_performance': analise.nota_performance.split()[-1][:-1] or 0,
                      'nota_experiencia': analise.nota_experiencia.split()[-1][:-1] or 0,
                      'nota_formacao_academica': analise.nota_formacao_academica.split()[-1][:-1] or 0,
                      'nota_especializacao': analise.nota_especializacao.split()[-1][:-1] or 0,
                      'nota_curso': analise.nota_curso.split()[-1][:-1] or 0,
                      'nota_idioma': analise.nota_idioma.split()[-1][:-1] or 0,
                      'nota_teste_comportamental': analise.nota_teste_psicologico.split()[-1][:-1] or 0
                  })

@staff_member_required
def avaliacao_desempenho(request):
    pessoas = Pessoa.objects.filter(cargo__isnull=False)

    obj_pessoa = None
    avaliacao_gestor = None
    autoavaliacao = None
    avaliacoes_subordinados = None
    avaliacoes_pares = None
    itens_competencia = None

    if request.method == 'POST':
        pessoa = request.POST['pessoa']
        obj_pessoa = Pessoa.objects.get(pk=pessoa)

        avaliacao_gestor = AvaliacaoDesempenho.objects.filter(
            pessoa=pessoa,
            respondida=True, 
            tipo_avaliacao='subordinado'
        ).last()

        autoavaliacao = AvaliacaoDesempenho.objects.filter(
            pessoa=pessoa,
            respondida=True, 
            tipo_avaliacao='autoavaliacao'
        ).last()

        avaliacoes_subordinados = AvaliacaoDesempenho.objects.media_competencias(pessoa,'gestor')

        avaliacoes_pares = AvaliacaoDesempenho.objects.media_competencias(pessoa,'par')

        itens_competencia = obj_pessoa.notas_por_competencia()

    return render(request, 'dashboard/avaliacao_desempenho.html',
                    {
                        'pessoas': pessoas,
                        'pessoa': obj_pessoa,
                        'avaliacao_gestor': avaliacao_gestor,
                        'autoavaliacao': autoavaliacao,
                        'avaliacoes_subordinados': avaliacoes_subordinados,
                        'avaliacoes_pares': avaliacoes_pares,
                        'itens_competencia': itens_competencia
                    }
                )


@staff_member_required
def relatorio_genero(request):
    pessoas = Pessoa.objects.all()
    total = pessoas.count()
    pessoas = pessoas.values('sexo').annotate(quantidade=Count('pk')).order_by('sexo')

    return render(
        request, 
        'dashboard/genero.html',
        {
            'pessoas': pessoas,
            'total': total
        }
    )

@staff_member_required
def relatorio_faixa_etaria(request):
    nao_informado = 0
    ate_20 = 0
    entre_21_25 = 0
    entre_26_30 = 0
    entre_31_35 = 0
    entre_36_40 = 0
    entre_41_45 = 0
    entre_46_50 = 0
    entre_51_55 = 0
    entre_56_60 = 0
    acima_60 = 0

    pessoas = Pessoa.objects.all()
    total = pessoas.count()

    for pessoa in pessoas:
        if pessoa.idade:
            if pessoa.idade <= 20:
                ate_20 += 1
            elif pessoa.idade >= 21 and pessoa.idade <= 25:
                entre_21_25 += 1
            elif pessoa.idade >= 26 and pessoa.idade <= 30:
                entre_26_30 += 1
            elif pessoa.idade >= 31 and pessoa.idade <= 35:
                entre_31_35 += 1
            elif pessoa.idade >= 36 and pessoa.idade <= 40:
                entre_36_40 += 1
            elif pessoa.idade >= 41 and pessoa.idade <= 45:
                entre_41_45 += 1
            elif pessoa.idade >= 46 and pessoa.idade <= 50:
                entre_46_50 += 1
            elif pessoa.idade >= 51 and pessoa.idade <= 55:
                entre_51_55 += 1
            elif pessoa.idade >= 56 and pessoa.idade <= 60:
                entre_56_60 += 1
            elif pessoa.idade > 60:
                acima_60 += 1
        else:
            nao_informado += 1

    return render(
        request, 
        'dashboard/faixa_etaria.html',
        {
            'nao_informado': nao_informado,
            'ate_20': ate_20,
            'entre_21_25': entre_21_25,
            'entre_26_30': entre_26_30,
            'entre_31_35': entre_31_35,
            'entre_36_40': entre_36_40,
            'entre_41_45': entre_41_45,
            'entre_46_50': entre_46_50,
            'entre_51_55': entre_51_55,
            'entre_56_60': entre_56_60,
            'acima_60': acima_60,
            'total': total,
        }
    )

@staff_member_required
def relatorio_estado_civil(request):
    pessoas = Pessoa.objects.all()
    total = pessoas.count()
    pessoas = pessoas.values('estado_civil__nome').annotate(quantidade=Count('*')).order_by('estado_civil__nome')

    return render(
        request, 
        'dashboard/estado_civil.html',
        {
            'pessoas': pessoas,
            'total': total
        }
    )

@staff_member_required
def relatorio_filhos(request):
    pessoas = Pessoa.objects.all()
    sem_filhos = 0
    com_filhos_1 = 0
    com_filhos_2 = 0
    com_filhos_3 = 0
    com_filhos_4_ou_mais = 0
    total = pessoas.count()

    for pessoa in pessoas:
        quantidade_filhos = len(pessoa.filho_set.all())

        if quantidade_filhos == 0:
            sem_filhos += 1
        elif quantidade_filhos == 1:
            com_filhos_1 += 1
        elif quantidade_filhos == 2:
            com_filhos_2 += 1
        elif quantidade_filhos == 3:
            com_filhos_3 += 1
        elif quantidade_filhos >= 4:
            com_filhos_4_ou_mais += 1

    return render(
        request, 
        'dashboard/filhos.html',
        {
            'pessoas': pessoas,
            'sem_filhos': sem_filhos,
            'com_filhos_1': com_filhos_1,
            'com_filhos_2': com_filhos_2,
            'com_filhos_3': com_filhos_3,
            'com_filhos_4_ou_mais': com_filhos_4_ou_mais,
            'total': total
        }
    )

@staff_member_required
def relatorio_cidade(request):
    pessoas = Pessoa.objects.all()
    total = pessoas.count()
    pessoas = pessoas.values('cidade').annotate(quantidade=Count('*')).order_by('cidade')

    return render(
        request, 
        'dashboard/cidade.html',
        {
            'pessoas': pessoas,
            'total': total
        }
    )

@staff_member_required
def relatorio_curso(request):
    pessoas = Pessoa.objects.all().count()
    cursos = Curso.objects.all().count()
    media_cursos = cursos/pessoas

    return render(
        request, 
        'dashboard/curso.html',
        {
            'media_cursos': media_cursos,
            'pessoas': pessoas,
            'cursos': cursos,
        }
    )

@staff_member_required
def relatorio_titulacao(request):
    import collections

    pessoas = Pessoa.objects.all()
    total = pessoas.count()

    itens_resultado = [pessoa.titulacao for pessoa in pessoas]

    resultado = {item: itens_resultado.count(item) for item in itens_resultado}

    resultado_ordenado = collections.OrderedDict(sorted(resultado.items()))

    return render(
        request, 
        'dashboard/titulacao.html',
        {
            'pessoas': pessoas,
            'total': total,
            'resultado': resultado_ordenado
        }
    )

@staff_member_required
def relatorio_idiomas(request):
    idiomas = Idioma.objects.all()
    total = idiomas.count()
    idiomas = idiomas.values('idioma', 'nivel').annotate(quantidade=Count('pk')).order_by('idioma', 'nivel')

    return render(
        request, 
        'dashboard/idiomas.html',
        {
            'idiomas': idiomas,
            'total': total
        }
    )

@staff_member_required
def relatorio_atuacao_profissional(request):
    pessoas = Pessoa.objects.all()
    total = pessoas.count()
    preenchido = 0
    nao_preenchido = 0
    preencheram = []
    nao_preencheram = []

    for pessoa in pessoas:
        if len(pessoa.experienciaprofissional_set.all()) > 0:
            preenchido += 1
            preencheram.append(pessoa)
        else:
            nao_preenchido += 1
            nao_preencheram.append(pessoa)

    return render(
        request, 
        'dashboard/atuacao_profissional.html',
        {
            'pessoas': pessoas,
            'preenchido': preenchido,
            'nao_preenchido': nao_preenchido,
            'total': total,
            'preencheram': preencheram,
            'nao_preencheram': nao_preencheram,
        }
    )

@staff_member_required
def relatorio_estatistica_geral(request):
    avaliacoes_desempenho = AvaliacaoDesempenho.objects.all()
    avaliacoes_respondidas = avaliacoes_desempenho.filter(respondida=True)
    avaliacoes_pendentes = avaliacoes_desempenho.exclude(respondida=True)

    quantidade_respondida = avaliacoes_desempenho.filter(respondida=True).count()

    maior_nota = 0
    menor_nota = 100
    melhor_avaliacao = None
    pior_avaliacao = None
    total_notas = 0

    for avaliacao in avaliacoes_respondidas:
        total_notas += avaliacao.nota_competencias if avaliacao.nota_competencias else 0

        if avaliacao.nota_competencias:
            if avaliacao.nota_competencias > maior_nota:
                melhor_avaliacao = avaliacao
                maior_nota = avaliacao.nota_competencias
            
            if avaliacao.nota_competencias < menor_nota:
                pior_avaliacao = avaliacao
                menor_nota = avaliacao.nota_competencias

    media_geral = total_notas/quantidade_respondida if quantidade_respondida > 0 else 0

    # Resultado de itens de competência
    Resultado = namedtuple(
        'Resultado', 
        'competencia autoavaliacao gestor pares subordinados total'
    )

    itens_competencia = ItemCompetencia.objects.filter(
        avaliacao_desempenho__respondida=True
    )
    
    competencias = Competencia.objects.all()
    
    resultado = []

    for competencia in competencias:
        itens_totais = itens_competencia.filter(competencia=competencia)
        media_total = itens_totais.aggregate(Avg('nota'))['nota__avg']

        itens_autoavaliacao = itens_competencia.filter(avaliacao_desempenho__tipo_avaliacao='autoavaliacao',competencia=competencia)
        media_autoavaliacao = itens_autoavaliacao.aggregate(Avg('nota'))['nota__avg']

        itens_gestor = itens_competencia.filter(avaliacao_desempenho__tipo_avaliacao='subordinado',competencia=competencia)
        media_gestor = itens_gestor.aggregate(Avg('nota'))['nota__avg']

        itens_subordinado = itens_competencia.filter(avaliacao_desempenho__tipo_avaliacao='gestor',competencia=competencia)
        media_subordinados = itens_subordinado.aggregate(Avg('nota'))['nota__avg']

        itens_par = itens_competencia.filter(avaliacao_desempenho__tipo_avaliacao='par',competencia=competencia)
        media_pares = itens_par.aggregate(Avg('nota'))['nota__avg']

        resultado.append(
            Resultado(
                competencia,
                media_autoavaliacao or 0,
                media_gestor or 0,
                media_pares or 0,
                media_subordinados or 0,
                media_total or 0
            )
        )

    
    return render(
        request, 
        'dashboard/estatistica_geral.html',
        {
            'avaliacoes_desempenho': avaliacoes_desempenho,
            'avaliacoes_pendentes': avaliacoes_pendentes,
            'quantidade_respondida': quantidade_respondida,
            'melhor_avaliacao': melhor_avaliacao,
            'pior_avaliacao': pior_avaliacao,
            'media_geral': media_geral,
            'itens_competencia': resultado
        }
    )


@staff_member_required
def relatorio_estatistica_gestor(request):
    pessoas = Pessoa.objects.all().order_by('nome')
    avaliacoes_desempenho = AvaliacaoDesempenho.objects.all()

    Resultado = namedtuple('Resultado', 'gestor total media maior_nota menor_nota')

    resultado_final = []

    for pessoa in pessoas:
        if pessoa.is_lider:
            avaliacoes_respondidas = avaliacoes_desempenho.filter(respondida=True, pessoa__gestor=pessoa.user)

            quantidade_respondida = avaliacoes_respondidas.count()

            maior_nota = 0
            menor_nota = 100
            melhor_avaliacao = None
            pior_avaliacao = None
            total_notas = 0

            for avaliacao in avaliacoes_respondidas:
                total_notas += avaliacao.nota_competencias if avaliacao.nota_competencias else 0

                if avaliacao.nota_competencias:
                    if avaliacao.nota_competencias > maior_nota:
                        melhor_avaliacao = avaliacao
                        maior_nota = avaliacao.nota_competencias
                    
                    if avaliacao.nota_competencias < menor_nota:
                        pior_avaliacao = avaliacao
                        menor_nota = avaliacao.nota_competencias

            media_geral = total_notas/quantidade_respondida if quantidade_respondida > 0 else 0

            resultado_final.append(
                Resultado(
                    pessoa,
                    quantidade_respondida,
                    media_geral,
                    melhor_avaliacao,
                    pior_avaliacao
                )
            )

    return render(
        request, 
        'dashboard/estatistica_gestor.html',
        {
            'resultado_final': resultado_final,
        }
    )


@staff_member_required
def relatorio_estatistica_genero(request):
    avaliacoes_desempenho = AvaliacaoDesempenho.objects.all()
    avaliacoes_respondidas = avaliacoes_desempenho.filter(respondida=True)
    
    Resultado = namedtuple('Resultado', 'genero total media maior_nota menor_nota')

    resultado_final = []


    avaliacoes_respondidas_masculino = avaliacoes_respondidas.filter(pessoa__sexo='MAS')
    quantidade_respondida_masculino = avaliacoes_respondidas_masculino.count()
    maior_nota_masculino = 0
    menor_nota_masculino = 100
    melhor_avaliacao_masculino = None
    pior_avaliacao_masculino = None
    total_notas_masculino = 0

    for avaliacao in avaliacoes_respondidas_masculino:
        total_notas_masculino += avaliacao.nota_competencias if avaliacao.nota_competencias else 0

        if avaliacao.nota_competencias:
            if avaliacao.nota_competencias > maior_nota_masculino:
                melhor_avaliacao_masculino = avaliacao
                maior_nota_masculino = avaliacao.nota_competencias
            
            if avaliacao.nota_competencias < menor_nota_masculino:
                pior_avaliacao_masculino = avaliacao
                menor_nota_masculino = avaliacao.nota_competencias

    media_geral_masculino = total_notas_masculino/quantidade_respondida_masculino if quantidade_respondida_masculino > 0 else 0

    resultado_final.append(
        Resultado(
            'Masculino',
            quantidade_respondida_masculino,
            media_geral_masculino,
            melhor_avaliacao_masculino,
            pior_avaliacao_masculino
        )
    )

    avaliacoes_respondidas_feminino = avaliacoes_respondidas.filter(pessoa__sexo='FEM')
    quantidade_respondida_feminino = avaliacoes_respondidas_feminino.count()
    maior_nota_feminino = 0
    menor_nota_feminino = 100
    melhor_avaliacao_feminino = None
    pior_avaliacao_feminino = None
    total_notas_feminino = 0

    for avaliacao in avaliacoes_respondidas_feminino:
        total_notas_feminino += avaliacao.nota_competencias if avaliacao.nota_competencias else 0

        if avaliacao.nota_competencias:
            if avaliacao.nota_competencias > maior_nota_feminino:
                melhor_avaliacao_feminino = avaliacao
                maior_nota_feminino = avaliacao.nota_competencias
            
            if avaliacao.nota_competencias < menor_nota_feminino:
                pior_avaliacao_feminino = avaliacao
                menor_nota_feminino = avaliacao.nota_competencias

    media_geral_feminino = total_notas_feminino/quantidade_respondida_feminino if quantidade_respondida_feminino > 0 else 0

    resultado_final.append(
        Resultado(
            'Feminino',
            quantidade_respondida_feminino,
            media_geral_feminino,
            melhor_avaliacao_feminino,
            pior_avaliacao_feminino
        )
    )

    return render(
        request, 
        'dashboard/estatistica_genero.html',
        {
            'resultado_final': resultado_final,
        }
    )


@staff_member_required
def relatorio_estatistica_faixa_etaria(request):
    resultado_final = AvaliacaoDesempenho.objects.resultado_avaliacao_faixa_etaria()
    
    return render(
        request, 
        'dashboard/estatistica_faixa_etaria.html',
        {
            'resultado_final': resultado_final,
        }
    )


@staff_member_required
def relatorio_estatistica_liderados(request):
    liderados = Pessoa.objects.filter(gestor__isnull=False)

    lideres = [pessoa.gestor for pessoa in liderados.order_by('gestor__pessoa__nome')]
    lideres = list(set(lideres))
    lideres.sort(key=lambda x:x.pessoa.nome)
    
    gestor = request.user

    if request.method == 'POST':
        gestor = request.POST['gestor']

    liderados = liderados.filter(gestor=gestor).order_by('nome')

    resultado_final = []

    for pessoa in liderados:
        resultado_final.append(AvaliacaoDesempenho.objects.resultado_liderados(pessoa))
    
    return render(
        request, 
        'dashboard/estatistica_resultado_liderados.html',
        {
            'resultado_final': resultado_final,
            'lideres': lideres,
            'gestor': gestor
        }
    )
