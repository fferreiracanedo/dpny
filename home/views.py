from collections import namedtuple
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core import serializers
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from django.urls import reverse_lazy
import base64
from django.db.models import Q
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from avaliacao_desempenho.models import AvaliacaoDesempenho
from avaliacao_desempenho.models import ItemMeta, ItemCompetencia
from configuracao_avaliacao_desempenho.models import Competencia
from core.models import EstadoCivil
from pessoa.models import Pessoa
from pessoa.forms import PessoaForm
from pessoa.models import ExperienciaProfissional
from pessoa.forms import ExperienciaProfissionalInlineFormSet
from pessoa.models import FormacaoAcademica
from pessoa.forms import FormacaoAcademicaInlineFormSet
from pessoa.models import Curso
from pessoa.models import RequisitoTecnico
from pessoa.models import Midia
from pessoa.forms import CursoInlineFormSet
from perfil.models import Perfil
from perfil.models import AnaliseTalento
from formacao.models import Idioma
from formacao.models import CargaHoraria
from formacao.models import Curso as CursoItem
from experiencia_profissional.models import Experiencia
from experiencia_profissional.models import Cargo
from pessoa.forms import IdiomaInlineFormSet
from teste_psicologico.forms import TestePsicologicoForm
from teste_psicologico.models import TestePsicologico
from teste_psicologico.models import Afirmativa
from teste_psicologico.models import Resposta
from perfil.models import ConfigAnaliseTalento
from pdi.models import Pdi, PdiCompetencia
from pdi.forms import PdiForm, PdiCompetenciaInlineFormSet
import json

@login_required
def home(request):
    pessoa = Pessoa.objects.filter(user=request.user.id).first()
    CargoIndicado = namedtuple('CargoIndicado', 'nota_total cargo descricao')

    if pessoa:
        pre_analises = AnaliseTalento.objects.filter(pessoa=pessoa, pre_analise=True)

        pre_analises = sorted([
            CargoIndicado(
                analise.nota_total.split()[-1] or '0%',
                analise.perfil.nome,
                analise.perfil.descricao
            ) for analise in pre_analises
        ], key=lambda x: float(x.nota_total.split()[-1][:-1] or 0), reverse=True)[0:5]
    else:
        pre_analises = None

    return render(request, 'index.html',{
        'pre_analises': pre_analises
    })


@login_required
def dados(request):
    pessoa = Pessoa.objects.filter(user=request.user.id).first()

    if request.method == 'POST':
        dados_json = request.POST.get('dados_pessoais')
        dados = json.loads(dados_json)

        if pessoa:
            pessoa.nome = dados['nome']
            pessoa.cpf = dados['cpf']
            pessoa.data_nascimento = dados['dataNascimento']
            pessoa.logradouro = dados['endereco']
            pessoa.bairro = dados['bairro']
            pessoa.cep = dados['cep']
            pessoa.cidade = dados['cidade']
            pessoa.estado = dados['estado']
            pessoa.estado_civil = dados['estadoCivil']
            pessoa.telefone = dados['telefoneCelular']
            pessoa.telefone2 = dados['telefoneResidencial']
            pessoa.email = dados['email']
            pessoa.ja_trabalhou = dados['jaTrabalhou']
            pessoa.pretensao_salarial = dados['pretensaoSalarial']
            pessoa.disponibilidade_viajar = dados['disponibilidadeViagem']
            pessoa.quando_trabalhou = dados['quandoTrabalhou']
            pessoa.projeto_trabalhou = dados['projeto']
            pessoa.link_perfil_linkedin = dados['perfilLinkedin']

            pessoa.save()
        else:
            pessoa = Pessoa(
                nome = dados['nome'],
                cpf = dados['cpf'],
                data_nascimento = dados['dataNascimento'],
                logradouro = dados['endereco'],
                bairro = dados['bairro'],
                cep = dados['cep'],
                cidade = dados['cidade'],
                estado = dados['estado'],
                estado_civil = dados['estadoCivil'],
                telefone = dados['telefoneCelular'],
                telefone2 = dados['telefoneResidencial'],
                email = dados['email'],
                ja_trabalhou = dados['jaTrabalhou'],
                pretensao_salarial = dados['pretensaoSalarial'],
                disponibilidade_viajar = dados['disponibilidadeViagem'],
                quando_trabalhou = dados['quandoTrabalhou'],
                projeto_trabalhou = dados['projeto'],
                link_perfil_linkedin = dados['perfilLinkedin'],
                user = request.user
            )

            pessoa.save()

    estados_civis = EstadoCivil.objects.all()

    return render(
        request,
        'dados_pessoais.html', {
            'pessoa': pessoa,
            'estados_civis': estados_civis,
        }
    )

@login_required
def experiencia_profissional(request):
    pessoa = Pessoa.objects.filter(user=request.user.id).first()

    if not pessoa:
        return redirect('dados')

    if request.method == 'POST':
        experiencia_profissional_json = request.POST.get('experiencia_profissional', "")
        midias_json = request.POST.get('midias', "")

        experiencias = json.loads(experiencia_profissional_json)
        midias = json.loads(midias_json)
        
        for experiencia in experiencias:
            cargo = Cargo.objects.get(pk=experiencia['cargo'])

            data_inicio = experiencia['dataInicio'] if experiencia['dataInicio'] != '' else None
            data_termino = experiencia['dataSaida'] if experiencia['dataSaida'] != '' else None

            try:
                obj_experiencia = ExperienciaProfissional.objects.get(pk=experiencia['formIndex'])
                obj_experiencia.empresa = experiencia['nomeEmpresa']
                obj_experiencia.cargo = cargo
                obj_experiencia.data_inicio = data_inicio
                obj_experiencia.data_termino = data_termino
                obj_experiencia.save()
            except:
                nova_experiencia = ExperienciaProfissional(
                    empresa = experiencia['nomeEmpresa'],
                    cargo = cargo,
                    data_inicio = data_inicio,
                    data_termino = data_termino,
                    pessoa=pessoa
                )
                nova_experiencia.save()

        for midia in midias:
            arquivo = None
            if midia.get('foto'):
                arquivo = base64_file(data=midia['foto'], name=midia['titulo'])

            try:
                obj_midia = Midia.objects.get(pk=midia['mediaIndex'])
                obj_midia.titulo = midia['titulo']
                obj_midia.descricao = midia['descricao']
                obj_midia.link = midia['link']
                obj_midia.data_criacao = midia['dataInsercao']
                obj_midia.arquivo = arquivo if arquivo else obj_midia.arquivo
                obj_midia.save()
            except:
                nova_midia = Midia(
                    titulo = midia['titulo'],
                    descricao = midia['descricao'],
                    link = midia['link'],
                    data_criacao = midia['dataInsercao'],
                    arquivo = arquivo,
                    pessoa=pessoa
                )

                nova_midia.save()

        retorno_experiencias = ExperienciaProfissional.objects.filter(pessoa=pessoa.id)
        experiencias_serializadas = serializers.serialize('json', retorno_experiencias)
        return JsonResponse(experiencias_serializadas, safe=False)
    else:
        experiencias = ExperienciaProfissional.objects.filter(pessoa=pessoa.id)
        cargos = Cargo.objects.all()
        midias = Midia.objects.filter(pessoa=pessoa.id)
            
        return render(
            request,
            'experiencia_profissional.html',
            {
                'pessoa': pessoa,
                'experiencias': experiencias,
                'cargos': cargos,
                'midias': midias
            }
        )


@login_required
def excluir_experiencia_profissional(request):
    if request.method == 'POST':
        id_experiencia_profissional = request.POST.get('experiencia_profissional', None)

        try:
            ExperienciaProfissional.objects.get(pk=id_experiencia_profissional).delete()

            retorno = {
                'retorno': 'Sucesso!'
            }
        except:
            retorno = {
                'retorno': 'Erro ao excluir!'
            }
        
        return JsonResponse(retorno)


@login_required
def formacao_academica(request):
    pessoa = Pessoa.objects.filter(user=request.user.id).first()

    if not pessoa:
        return redirect('dados')

    if request.method == 'POST':
        formacao_academica_json = request.POST.get('formacao_academica', "")
        formacoes = json.loads(formacao_academica_json)
        
        for formacao in formacoes:
            certificado = None
            if formacao.get('midia'):
                certificado = base64_file(data=formacao['midia']['foto'], name="Certificado")
            
            curso_item = CursoItem.objects.get(pk=formacao['curso'])

            data_inicio = formacao['dataInicio'] if formacao['dataInicio'] != '' else None
            data_termino = formacao['dataTermino'] if formacao['dataTermino'] != '' else None

            try:
                obj_formacao = FormacaoAcademica.objects.get(pk=formacao['formIndex'])
                obj_formacao.curso = curso_item
                obj_formacao.instituicao = formacao['instituicao']
                obj_formacao.nivel_escolaridade = formacao['nivelEscolaridade']
                obj_formacao.situacao = formacao['situacao']
                obj_formacao.data_inicio = data_inicio
                obj_formacao.data_termino = data_termino
                obj_formacao.certificado = certificado if certificado else obj_formacao.certificado
                obj_formacao.save()
            except:
                nova_formacao = FormacaoAcademica(
                    curso = curso_item,
                    instituicao = formacao['instituicao'],
                    nivel_escolaridade = formacao['nivelEscolaridade'],
                    situacao = formacao['situacao'],
                    data_inicio = data_inicio,
                    data_termino = data_termino,
                    certificado = certificado,
                    pessoa=pessoa
                )
                nova_formacao.save()

        retorno_formacoes = FormacaoAcademica.objects.filter(pessoa=pessoa.id)
        formacoes_serializadas = serializers.serialize('json', retorno_formacoes)
        return JsonResponse(formacoes_serializadas, safe=False)
    else:
        formacoes = FormacaoAcademica.objects.filter(pessoa=pessoa.id)
        list_curso = CursoItem.objects.all()
            
        return render(
            request,
            'formacao_academica.html',
            {
                'pessoa': pessoa,
                'formacoes': formacoes,
                'list_curso': list_curso,
            }
        )


@login_required
def excluir_formacao_academica(request):
    if request.method == 'POST':
        id_formacao_academica = request.POST.get('formacao_academica', None)

        try:
            FormacaoAcademica.objects.get(pk=id_formacao_academica).delete()

            retorno = {
                'retorno': 'Sucesso!'
            }
        except:
            retorno = {
                'retorno': 'Erro ao excluir!'
            }
        
        return JsonResponse(retorno)


@login_required
def excluir_certificado_formacao_academica(request):
    if request.method == 'POST':
        id_formacao_academica = request.POST.get('formacao_academica', None)

        try:
            formacao_academica = FormacaoAcademica.objects.get(pk=id_formacao_academica)

            formacao_academica.certificado = None

            formacao_academica.save()

            retorno = {
                'retorno': 'Sucesso!'
            }
        except:
            retorno = {
                'retorno': 'Erro ao excluir!'
            }
        
        return JsonResponse(retorno)


@login_required
def cursos(request):
    pessoa = Pessoa.objects.filter(user=request.user.id).first()

    if not pessoa:
        return redirect('dados')
    
    if request.method == 'POST':
        cursos_json = request.POST.get('cursos', "")
        cursos = json.loads(cursos_json)
        
        for curso in cursos:
            certificado = None
            if curso.get('midia'):
                certificado = base64_file(data=curso['midia']['foto'], name="Certificado")
            
            curso_item = CursoItem.objects.get(pk=curso['curso'])

            data_inicio = curso['dataInicio'] if curso['dataInicio'] != '' else None
            data_termino = curso['dataTermino'] if curso['dataTermino'] != '' else None

            try:
                obj_curso = Curso.objects.get(pk=curso['formIndex'])
                obj_curso.curso = curso_item
                obj_curso.instituicao = curso['instituicao']
                obj_curso.carga_horaria = curso['cargaHoraria']
                obj_curso.data_inicio = data_inicio
                obj_curso.data_termino = data_termino
                obj_curso.certificado = certificado if certificado else obj_curso.certificado
                obj_curso.save()
            except:
                novo_curso = Curso(
                    curso = curso_item,
                    instituicao = curso['instituicao'],
                    carga_horaria = curso['cargaHoraria'],
                    data_inicio = data_inicio,
                    data_termino = data_termino,
                    certificado = certificado,
                    pessoa=pessoa
                )
                novo_curso.save()

        retorno_cursos = Curso.objects.filter(pessoa=pessoa.id)
        cursos_serializados = serializers.serialize('json', retorno_cursos)
        return JsonResponse(cursos_serializados, safe=False)
    else:
        cursos = Curso.objects.filter(pessoa=pessoa.id)
        list_curso = CursoItem.objects.all()
        list_carga_horaria = CargaHoraria.objects.all()
            
        return render(
            request,
            'cursos.html',
            {
                'pessoa': pessoa,
                'cursos': cursos,
                'list_curso': list_curso,
                'list_carga_horaria': list_carga_horaria,
            }
        )


@login_required
def excluir_curso(request):
    if request.method == 'POST':
        id_curso = request.POST.get('curso', None)

        try:
            Curso.objects.get(pk=id_curso).delete()

            retorno = {
                'retorno': 'Sucesso!'
            }
        except:
            retorno = {
                'retorno': 'Erro ao excluir!'
            }
        
        return JsonResponse(retorno)


@login_required
def excluir_certificado_curso(request):
    if request.method == 'POST':
        id_curso = request.POST.get('curso', None)

        try:
            curso = Curso.objects.get(pk=id_curso)

            curso.certificado = None

            curso.save()

            retorno = {
                'retorno': 'Sucesso!'
            }
        except:
            retorno = {
                'retorno': 'Erro ao excluir!'
            }
        
        return JsonResponse(retorno)


@login_required
def idiomas(request):
    pessoa = Pessoa.objects.filter(user=request.user.id).first()

    if not pessoa:
        return redirect('dados')
    
    if request.method == 'POST':
        idiomas_json = request.POST.get('idiomas', "")
        idiomas = json.loads(idiomas_json)
        
        for idioma in idiomas:
            certificado = None
            if idioma.get('midia'):
                certificado = base64_file(data=idioma['midia']['foto'], name="Certificado")

            try:
                obj_idioma = Idioma.objects.get(pk=idioma['formIndex'])
                obj_idioma.idioma = idioma['idioma']
                obj_idioma.nivel = idioma['nivel']
                obj_idioma.certificado = certificado if certificado else obj_idioma.certificado
                obj_idioma.save()
            except:
                novo_idioma = Idioma(
                    idioma=idioma['idioma'], 
                    pessoa=pessoa, 
                    nivel=idioma['nivel'],
                    certificado=certificado
                    )
                novo_idioma.save()

        retorno_idiomas = Idioma.objects.filter(pessoa=pessoa.id)
        idiomas_serializados = serializers.serialize('json', retorno_idiomas)
        return JsonResponse(idiomas_serializados, safe=False)
    else:
        idiomas = Idioma.objects.filter(pessoa=pessoa.id)
            
        return render(
            request,
            'idiomas.html',
            {
                'pessoa': pessoa,
                'idiomas': idiomas
            }
        )

@login_required
def excluir_idioma(request):
    if request.method == 'POST':
        id_idioma = request.POST.get('idioma', None)

        try:
            Idioma.objects.get(pk=id_idioma).delete()

            retorno = {
                'retorno': 'Sucesso!'
            }
        except:
            retorno = {
                'retorno': 'Erro ao excluir!'
            }
        
        return JsonResponse(retorno)


@login_required
def excluir_midia(request):
    if request.method == 'POST':
        id_midia = request.POST.get('midia', None)

        try:
            Midia.objects.get(pk=id_midia).delete()

            retorno = {
                'retorno': 'Sucesso!'
            }
        except:
            retorno = {
                'retorno': 'Erro ao excluir!'
            }
        
        return JsonResponse(retorno)


@login_required
def excluir_certificado_idioma(request):
    if request.method == 'POST':
        id_idioma = request.POST.get('idioma', None)

        try:
            idioma = Idioma.objects.get(pk=id_idioma)

            idioma.certificado = None

            idioma.save()

            retorno = {
                'retorno': 'Sucesso!'
            }
        except:
            retorno = {
                'retorno': 'Erro ao excluir!'
            }
        
        return JsonResponse(retorno)


@login_required
def requisitos_tecnicos(request):
    pessoa = Pessoa.objects.filter(user=request.user.id).first()

    if not pessoa:
        return redirect('dados')

    
    requisitos_tecnicos = RequisitoTecnico.objects.all()
        
    return render(
        request,
        'requisitos_tecnicos.html',
        {
            'pessoa': pessoa,
            'requisitos_tecnicos': requisitos_tecnicos
        }
    )


@login_required
def perfis(request):
    if request.user.is_staff:
        perfis = Perfil.objects.filter(Q(gestor=request.user) | Q(gestor=None))
    else:
        pessoa = Pessoa.objects.filter(user=request.user.id).first()
        if pessoa.cargo:
            perfis = Perfil.objects.filter(visualizar_site=True, visualizar_funcionarios=True)
        else:
            perfis = Perfil.objects.filter(visualizar_site=True)

    return render(request, 'perfis_disponiveis.html', {'perfis': perfis})


@login_required
def analises(request):
    if request.method == 'POST':
        pass
    else:
        pessoa = Pessoa.objects.filter(user=request.user.id).first()

        if pessoa:
            analises = AnaliseTalento.objects.filter(visivel_site=True, pessoa_id=pessoa.id)
        else:
            analises = None

        return render(request, 'analise_talento.html', {'analises': analises})


@login_required
def correlacionar(request, perfil):
    if request.method == 'POST':
        pass
    else:
        pessoa = Pessoa.objects.filter(user=request.user.id).first()
        
        if pessoa:
            perfil_obj = Perfil.objects.get(id=perfil)

            analise = AnaliseTalento(perfil=perfil_obj, pessoa=pessoa)
            analise.save()

            return render(request, 'correlacionar.html')
        else:
            return perfis(request)

@login_required
def teste_psicologico(request):
    pessoa = Pessoa.objects.filter(user=request.user.id).first()

    if not pessoa:
        return redirect('dados')

    teste_psicologico = TestePsicologico.objects.filter(pessoa=pessoa.id, respondido=False).first()

    return render(request, 'teste_psicologico.html', {
            'teste_psicologico': teste_psicologico,
            'pessoa': pessoa
        }
    )


@login_required
def curriculo(request, pessoa):
    pessoa = Pessoa.objects.get(pk=pessoa)

    return render(request, 'curriculo.html', {
            'pessoa': pessoa
        }
    )


@login_required
def respostas(request, teste_escrito):
    teste = TestePsicologico.objects.get(pk=teste_escrito)

    return render(request, 'respostas.html', {
            'teste': teste
        }
    )


@login_required
def ranking(request, perfil):
    perfil = Perfil.objects.get(pk=perfil)

    return render(request, 'ranking.html', {
            'perfil': perfil
        }
    )


@login_required
def avaliacoes_dashboard(request):
    avaliacoes_pendentes_autoavaliacao = AvaliacaoDesempenho.objects.filter(
        avaliador=request.user,
        tipo_avaliacao='autoavaliacao',
        respondida=False
    ).count()

    avaliacoes_concluidas_autoavaliacao = AvaliacaoDesempenho.objects.filter(
        avaliador=request.user,
        tipo_avaliacao='autoavaliacao',
        respondida=True
    ).count()

    avaliacoes_pendentes_gestor = AvaliacaoDesempenho.objects.filter(
        avaliador=request.user,
        tipo_avaliacao='gestor',
        respondida=False
    ).count()

    avaliacoes_concluidas_gestor = AvaliacaoDesempenho.objects.filter(
        avaliador=request.user,
        tipo_avaliacao='gestor',
        respondida=True
    ).count()

    avaliacoes_pendentes_subordinados = AvaliacaoDesempenho.objects.filter(
        avaliador=request.user,
        tipo_avaliacao='subordinado',
        respondida=False
    ).count()

    avaliacoes_concluidas_subordinados = AvaliacaoDesempenho.objects.filter(
        avaliador=request.user,
        tipo_avaliacao='subordinado',
        respondida=True
    ).count()

    avaliacoes_pendentes_pares = AvaliacaoDesempenho.objects.filter(
        avaliador=request.user,
        tipo_avaliacao='par',
        respondida=False
    ).count()

    avaliacoes_concluidas_pares = AvaliacaoDesempenho.objects.filter(
        avaliador=request.user,
        tipo_avaliacao='par',
        respondida=True
    ).count()

    total_autoavaliacao = avaliacoes_pendentes_autoavaliacao + avaliacoes_concluidas_autoavaliacao
    autoavaliacao = {
        'total': total_autoavaliacao,
        'pendentes': avaliacoes_pendentes_autoavaliacao,
        'concluidas': avaliacoes_concluidas_autoavaliacao,
        'porcentagem': int(avaliacoes_concluidas_autoavaliacao / total_autoavaliacao * 100) if total_autoavaliacao > 0 else 100
    }

    total_gestor = avaliacoes_pendentes_gestor + avaliacoes_concluidas_gestor
    gestor = {
        'total': total_gestor,
        'pendentes': avaliacoes_pendentes_gestor,
        'concluidas': avaliacoes_concluidas_gestor,
        'porcentagem': int(avaliacoes_concluidas_gestor / total_gestor * 100) if total_gestor > 0 else 100
    }

    total_subordinados = avaliacoes_pendentes_subordinados + avaliacoes_concluidas_subordinados
    subordinados = {
        'total': total_subordinados,
        'pendentes': avaliacoes_pendentes_subordinados,
        'concluidas': avaliacoes_concluidas_subordinados,
        'porcentagem': int(avaliacoes_concluidas_subordinados / total_subordinados * 100) if total_subordinados > 0 else 100
    }

    total_pares = avaliacoes_pendentes_pares + avaliacoes_concluidas_pares
    pares = {
        'total': total_pares,
        'pendentes': avaliacoes_pendentes_pares,
        'concluidas': avaliacoes_concluidas_pares,
        'porcentagem': int(avaliacoes_concluidas_pares / total_pares * 100) if total_pares > 0 else 100
    }

    return render(request, 'avaliacoes_dashboard.html', {
            'autoavaliacao': autoavaliacao,
            'gestor': gestor,
            'subordinados': subordinados,
            'pares': pares,
            'teste': 3.59
        }
    )


@login_required
def avaliacoes(request, tipo):
    avaliacoes_pendentes = AvaliacaoDesempenho.objects.filter(
        avaliador=request.user,
        tipo_avaliacao=tipo,
        respondida=False
    )

    avaliacoes_concluidas = AvaliacaoDesempenho.objects.filter(
        avaliador=request.user,
        tipo_avaliacao=tipo,
        respondida=True
    )

    total_avaliacoes = len(avaliacoes_pendentes) + len(avaliacoes_concluidas)

    if tipo == 'autoavaliacao':
        titulo = "Autoavaliação"
    elif tipo == 'gestor':
        titulo = "Avaliação de Gestor"
    elif tipo == 'subordinado':
        titulo = "Avaliação de Subordinados"
    elif tipo == 'par':
        titulo = "Avaliação de Pares"

    return render(request, 'avaliacoes.html', {
            'avaliacoes_pendentes': avaliacoes_pendentes,
            'avaliacoes_concluidas': avaliacoes_concluidas,
            'titulo': titulo,
            'total_avaliacoes': total_avaliacoes
        }
    )

@login_required
def potencial(request):
    avaliacoes_pendentes = AvaliacaoDesempenho.objects.filter(
        avaliador=request.user,
        tipo_avaliacao='subordinado',
        resposta_potencial__isnull=True
    )

    avaliacoes_concluidas = AvaliacaoDesempenho.objects.filter(
        avaliador=request.user,
        tipo_avaliacao='subordinado',
        resposta_potencial__isnull=False
    )

    total_avaliacoes = len(avaliacoes_pendentes) + len(avaliacoes_concluidas)

    return render(request, 'potencial.html', {
            'avaliacoes_pendentes': avaliacoes_pendentes,
            'avaliacoes_concluidas': avaliacoes_concluidas,
            'total_avaliacoes': total_avaliacoes
        }
    )

@login_required
def avaliacao(request, avaliacao, tipo):
    try:
        avaliacao = AvaliacaoDesempenho.objects.get(pk=avaliacao, avaliador=request.user)
    except AvaliacaoDesempenho.DoesNotExist:
        raise Http404("Avaliação de desempenho não existe")

    if tipo == 'competencias':
        template = 'competencias.html'
        titulo = 'Competências '
    elif tipo == 'metas':
        template = 'metas.html'
        titulo = 'Metas '
    elif tipo == 'potencial':
        template = 'potencial.html'
        titulo = 'Potencial '
    else:
        template = 'avaliacao.html'
    
    if avaliacao.tipo_avaliacao == 'autoavaliacao':
        titulo += "na Autoavaliação"
    elif avaliacao.tipo_avaliacao == 'gestor':
        titulo += "do Gestor"
    elif avaliacao.tipo_avaliacao == 'subordinado':
        titulo += "do Subordinado"
    elif avaliacao.tipo_avaliacao == 'par':
        titulo += "do Par"


    return render(request, template, {
            'titulo': titulo,
            'avaliacao': avaliacao
        }
    )

@login_required
def comite(request):
    quantidade_transicao = 0
    quantidade_atencao_imediata = 0
    quantidade_desenvolvimento = 0
    quantidade_estavel = 0
    quantidade_consistente = 0
    quantidade_sucessor = 0

    pessoa = request.GET.get('pessoa', '')
    quadrante = request.GET.get('quadrante', '')
    lider = request.GET.get('lider', '')

    if request.user.is_staff:
        avaliacoes = AvaliacaoDesempenho.objects.filter(
            resultado_comite__isnull=False,
            tipo_avaliacao='subordinado'
        )

        if pessoa:
            avaliacoes = avaliacoes.filter(
                pessoa__nome__contains = pessoa
            )
        
        if quadrante:
            avaliacoes = avaliacoes.filter(
                resultado_comite = quadrante
            )
        
        if lider:
            avaliacoes = avaliacoes.filter(
                pessoa__gestor__pessoa__nome__contains = lider
            )

        order = [None, '', 'TRA', 'ATI', 'DES', 'EST', 'CON', 'SUC']
        avaliacoes = sorted(avaliacoes, key=lambda x: order.index(x.resultado_comite))

        for avaliacao in avaliacoes:
            if avaliacao.resultado_comite == 'TRA':
                quantidade_transicao += 1
            elif avaliacao.resultado_comite == 'ATI':
                quantidade_atencao_imediata += 1
            elif avaliacao.resultado_comite == 'DES':
                quantidade_desenvolvimento += 1
            elif avaliacao.resultado_comite == 'EST':
                quantidade_estavel += 1
            elif avaliacao.resultado_comite == 'CON':
                quantidade_consistente += 1
            elif avaliacao.resultado_comite == 'SUC':
                quantidade_sucessor += 1
            else:
                quantidade_transicao += 1
    else:
        avaliacoes = None

    return render(request, 'comite.html', {
            'avaliacoes': avaliacoes,
            'quantidade_transicao': quantidade_transicao,
            'quantidade_atencao_imediata': quantidade_atencao_imediata,
            'quantidade_desenvolvimento': quantidade_desenvolvimento,
            'quantidade_estavel': quantidade_estavel,
            'quantidade_consistente': quantidade_consistente,
            'quantidade_sucessor': quantidade_sucessor,
            'pessoa': pessoa,
            'quadrante': quadrante,
            'lider': lider,
        }
    )


@login_required
def trilha(request):
    treinamentos = [
        {
            'id': 1,
            'nome': 'Automatize seu processo de treinamento.',
            'descricao': 'Como automatizar o seu processo de treinamento com a SIPClick.',
            'tipo': 'video',
            'file': 'curso-1.mp4'
        },
        {
            'id': 2,
            'nome': 'Como estimular a capacitação dos colaboradores',
            'descricao': 'Como fazer seus colaboradores se interessarem por capacitações',
            'tipo': 'arquivo',
            'file': 'curso-2.pptx'
        },
        {
            'id': 3,
            'nome': 'Otimize seu RH',
            'descricao': 'Otimize seu RH com a SIPClick.',
            'tipo': 'video',
            'file': 'curso-3.mp4'
        },
        {
            'id': 4,
            'nome': 'Como ser um RH estratégico',
            'descricao': 'Saiba como ser um RH estratégico',
            'tipo': 'arquivo',
            'file': 'curso-4.pdf'
        },
        {
            'id': 5,
            'nome': 'Treinamento Agile Presence',
            'descricao': 'Treinamento Agile Presence',
            'tipo': 'video',
            'file': 'curso-5.mp4'
        }
    ]
    return render(request, 'trilha.html', {'treinamentos': treinamentos})


@login_required
def treinamento(request, treinamento):
    obj_treinamento = {}

    if treinamento == 1:
        obj_treinamento = {
            'id': 1,
            'nome': 'Automatize seu processo de treinamento.',
            'descricao': 'Como automatizar o seu processo de treinamento com a SIPClick.',
            'tipo': 'video',
            'file': 'curso-1.mp4'
        }
    elif treinamento == 2:
        obj_treinamento = {
            'id': 2,
            'nome': 'Como estimular a capacitação dos colaboradores',
            'descricao': 'Como fazer seus colaboradores se interessarem por capacitações',
            'tipo': 'arquivo',
            'file': 'curso-2.pptx'
        }
    elif treinamento == 3:
        obj_treinamento = {
            'id': 3,
            'nome': 'Otimize seu RH',
            'descricao': 'Otimize seu RH com a SIPClick.',
            'tipo': 'video',
            'file': 'curso-3.mp4'
        }
    elif treinamento == 4:
        obj_treinamento = {
            'id': 4,
            'nome': 'Como ser um RH estratégico',
            'descricao': 'Saiba como ser um RH estratégico',
            'tipo': 'pdf',
            'file': 'curso-4.pdf'
        }
    elif treinamento == 5:
        obj_treinamento = {
            'id': 5,
            'nome': 'Treinamento Agile Presence',
            'descricao': 'Treinamento Agile Presence',
            'tipo': 'video',
            'file': 'curso-5.mp4'
        }

    return render(request, 'treinamento.html', {'treinamento': obj_treinamento})

@staff_member_required
def resultado_avaliacao(request):
    if request.user.pessoa:
        subordinados = AvaliacaoDesempenho.objects.media_competencias(request.user.pessoa,'gestor') or 0
        autoavaliacao = AvaliacaoDesempenho.objects.media_competencias(request.user.pessoa,'autoavaliacao') or 0
        pares = AvaliacaoDesempenho.objects.media_competencias(request.user.pessoa,'par') or 0
        gestor = AvaliacaoDesempenho.objects.media_competencias(request.user.pessoa,'subordinado') or 0

        itens_meta = ItemMeta.objects.filter(
            avaliacao_desempenho__pessoa=request.user.pessoa
        )

        itens_competencia = request.user.pessoa.notas_por_competencia()


        return render(request, 'resultado_avaliacao.html', {
            'subordinados': subordinados,
            'autoavaliacao': autoavaliacao,
            'pares': pares,
            'gestor': gestor,
            'itens_meta': itens_meta,
            'pessoa': request.user.pessoa,
            'itens_competencia': itens_competencia
        })
    else:
        raise Http404("Não há pessoa vinculada")

@staff_member_required
def resultado_equipe(request):
    if request.user.pessoa:
        avaliacoes = AvaliacaoDesempenho.objects.filter(
            pessoa__gestor=request.user,
            respondida=True,
            tipo_avaliacao='subordinado'
        )

        return render(request, 'resultado_equipe.html', {
            'avaliacoes': avaliacoes
        })
    else:
        raise Http404("Não há pessoa vinculada")

@staff_member_required
def resultado_avaliacao_individual(request, id_pessoa):
    pessoa = Pessoa.objects.filter(
        id=id_pessoa,
        gestor=request.user
    ).first()

    if pessoa:
        subordinados = AvaliacaoDesempenho.objects.media_competencias(pessoa,'gestor') or 0
        autoavaliacao = AvaliacaoDesempenho.objects.media_competencias(pessoa,'autoavaliacao') or 0
        pares = AvaliacaoDesempenho.objects.media_competencias(pessoa,'par') or 0
        gestor = AvaliacaoDesempenho.objects.media_competencias(pessoa,'subordinado') or 0

        itens_meta = ItemMeta.objects.filter(
            avaliacao_desempenho__pessoa=pessoa
        )

        itens_competencia = pessoa.notas_por_competencia()

        return render(request, 'resultado_avaliacao.html', {
            'pessoa': pessoa,
            'subordinados': subordinados,
            'autoavaliacao': autoavaliacao,
            'pares': pares,
            'gestor': gestor,
            'itens_meta': itens_meta,
            'itens_competencia': itens_competencia
        })
    else:
        raise Http404("Não há pessoa disponível")


@staff_member_required
def visualizar_pdi(request, id_pessoa):
    pessoa = Pessoa.objects.filter(
        id=id_pessoa,
        gestor=request.user
    ).first()

    if pessoa:
        pdi = Pdi.objects.filter(pessoa=pessoa).first()

        return render(request, 'pdi_detail.html', {'pessoa': pessoa, 'pdi': pdi})
    else:
        raise Http404("Não há PDI disponível")

class PdiUpdateView(UpdateView):
    model = Pdi
    decorators = [login_required]
    form_class = PdiForm

    def dispatch(self, request, *args, **kwargs):
        pdis = Pdi.objects.filter(pessoa=request.user.pessoa)

        if not pdis:
            raise Http404("Não há PDI para a pessoa vinculada")
        return super(PdiUpdateView, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Pdi, pessoa=self.request.user.pessoa)
    
    def get_success_url(self, **kwargs):         
        return reverse_lazy('atualizar_pdi',)

    def get_context_data(self, **kwargs):
        context = super(PdiUpdateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context['pdi_competencia'] = PdiCompetenciaInlineFormSet(self.request.POST, instance=self.object)
            context['pdi_competencia'].full_clean()
        else:
            if self.request.user.pessoa.is_lider:
                competencias_query = Competencia.objects.filter(
                    categoria='lider'
                )
            else:
                competencias_query = Competencia.objects.filter(
                    categoria='liderado'
                )
            
            context['pdi_competencia'] = PdiCompetenciaInlineFormSet(
                instance=self.object
            )

            for form in context['pdi_competencia']:
                form.fields['competencia'].queryset = competencias_query

        return context
    
    def form_valid(self, form):
        context = self.get_context_data(form=form)
        formset_pdi_competencia = context['pdi_competencia']

        if formset_pdi_competencia.is_valid():
            response = super().form_valid(form)

            formset_pdi_competencia.instance = self.object
            formset_pdi_competencia.save()

            return response
        else:
            return super().form_invalid(form)


def gerenciar_inline_form(inline_form):
    for form in inline_form:
        if form.is_valid():
            try:
                try:
                    if not form.cleaned_data['DELETE']:
                        form.save(commit=False)
                        form.save()
                    else:
                        form.instance.delete()
                except IntegrityError:
                    pass
            except KeyError:
                pass


def realizar_pre_analises(pessoa):
    perfis_pre_analise = Perfil.objects.filter(disponivel_pre_analise=True)
    pre_analises = AnaliseTalento.objects.filter(pessoa=pessoa, pre_analise=True)

    for pre_analise in pre_analises:
        pre_analise.delete()

    for perfil in perfis_pre_analise:
        analise = AnaliseTalento(pessoa=pessoa, perfil=perfil, pre_analise=True)
        analise.save()

def base64_file(data, name=None):
    _format, _img_str = data.split(';base64,')
    _name, ext = _format.split('/')
    if not name:
        name = _name.split(":")[-1]
    return ContentFile(base64.b64decode(_img_str), name='{}.{}'.format(name, ext))