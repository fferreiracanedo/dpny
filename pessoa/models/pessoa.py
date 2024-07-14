from django.db import models
from django.contrib.auth.models import User
from .requisito_tecnico import RequisitoTecnico
from core.models import Cidade
from core.models import Estado
from core.models import Filial
from core.models import Grupo
from core.models import EstadoCivil
from experiencia_profissional.models import Cargo
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from decouple import config
from django.utils.html import strip_tags
from collections import namedtuple
from django.db.models import Avg


class Pessoa(models.Model):
    SIM_NAO_CHOICES = (
        ('Sim', 'Sim'),
        ('Não', 'Não')
    )

    SEXO_CHOICES = (
        ('MAS', 'Masculino'),
        ('FEM', 'Feminino')
    )

    COR_PELE_CHOICES = (
        ('Branca', 'Branca'),
        ('Morena', 'Morena'),
        ('Parda', 'Parda'),
        ('Negra', 'Negra'),
    )

    nome = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        verbose_name="Nome Completo",
        help_text="Campo Obrigatório*"
    )

    cpf = models.CharField(
        max_length=14,
        verbose_name="CPF",
        unique=True,
        help_text="Campo Obrigatório*",
        blank=True, null=True,
    )

    cpf_anexo = models.FileField(
        verbose_name="CPF Digitalizado",
        upload_to="documentos/",
        blank=True
    )
    
    pis_numero = models.CharField(
        max_length=100,
        verbose_name="Número do PIS",
        blank=True, null=True
    )

    pis_anexo = models.FileField(
        verbose_name="PIS Digitalizado",
        upload_to="documentos/",
        blank=True
    )

    rg = models.CharField(
        max_length=50,
        verbose_name="RG",
        blank=True, null=True
    )

    rg_orgao_expedidor = models.CharField(
        max_length=100,
        verbose_name="Orgão Expedidor",
        blank=True, null=True
    )

    rg_data_expedicao = models.DateField(
        verbose_name="Data de Expedição",
        blank=True, null=True
    )

    rg_anexo = models.FileField(
        verbose_name="RG Digitalizado",
        upload_to="documentos/",
        blank=True
    )

    nascimento_anexo = models.FileField(
        verbose_name="Certidão de Nascimento Digitalizada",
        upload_to="documentos/",
        blank=True
    )

    casamento_anexo = models.FileField(
        verbose_name="Certidão de Casamento Digitalizada",
        upload_to="documentos/",
        blank=True
    )

    divorcio_anexo = models.FileField(
        verbose_name="Divorcio Digitalizado",
        upload_to="documentos/",
        blank=True
    )

    habilitacao_anexo = models.FileField(
        verbose_name="Habilitação Digitalizada",
        upload_to="documentos/",
        blank=True
    )

    residencia_anexo = models.FileField(
        verbose_name="Comprovante de Residência Digitalizado",
        upload_to="documentos/",
        blank=True
    )

    nacionalidade = models.CharField(
        max_length=100,
        verbose_name="Nacionalidade",
        blank=True, null=True
    )

    municipio_nascimento = models.CharField(
        max_length=150,
        verbose_name="Município de Nascimento",
        blank=True, null=True
    )

    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
        blank=True,
        null=True
    )

    cor = models.CharField(
        max_length=50,
        verbose_name="Cor",
        choices=COR_PELE_CHOICES,
        blank=True, null=True
    )

    sexo = models.CharField(
        max_length=3,
        verbose_name="Sexo",
        choices=SEXO_CHOICES,
        blank=True, null=True
    )

    titulo_eleitor = models.CharField(
        max_length=150,
        verbose_name="Título de Eleitor",
        blank=True, null=True
    )

    titulo_eleitor_zona = models.CharField(
        max_length=50,
        verbose_name="Zona",
        blank=True, null=True
    )

    titulo_eleitor_secao = models.CharField(
        max_length=50,
        verbose_name="Seção",
        blank=True, null=True
    )

    titulo_eleitor_anexo = models.FileField(
        verbose_name="Título de Eleitor Digitalizado",
        upload_to="documentos/",
        blank=True
    )

    ctps_numero = models.CharField(
        max_length=100,
        verbose_name="CTPS",
        blank=True, null=True
    )

    ctps_serie = models.CharField(
        max_length=50,
        verbose_name="Série",
        blank=True, null=True
    )

    ctps_data_expedicao = models.DateField(
        verbose_name="Data de Expedição",
        blank=True, null=True
    )

    ctps_uf = models.CharField(
        max_length=2,
        verbose_name="UF",
        blank=True, null=True
    )

    ctps_anexo = models.FileField(
        verbose_name="CTPS Digitalizada",
        upload_to="documentos/",
        blank=True
    )

    nome_mae = models.CharField(
        max_length=150,
        verbose_name="Nome da Mãe",
        blank=True, null=True
    )

    nome_pai = models.CharField(
        max_length=150,
        verbose_name="Nome do Pai",
        blank=True, null=True
    )

    habilitacao_numero = models.CharField(
        max_length=100,
        verbose_name="Número da Habilitação",
        blank=True, null=True
    )

    habilitacao_categoria = models.CharField(
        max_length=10,
        verbose_name="Categoria",
        blank=True, null=True
    )

    logradouro = models.CharField(
        max_length=200,
        verbose_name="Endereço Residencial",
        help_text="Campo Obrigatório*",
        blank=True, null=True,
    )

    numero_endereco = models.CharField(
        max_length=50,
        verbose_name="Número",
        blank=True, null=True
    )

    complemento = models.CharField(
        max_length=100,
        verbose_name="Complemento",
        blank=True, null=True
    )

    bairro = models.CharField(
        max_length=200,
        verbose_name="Bairro",
        help_text="Campo Obrigatório*",
        blank=True, null=True,
    )

    cep = models.CharField(
        max_length=9,
        verbose_name="CEP",
        help_text="Campo Obrigatório*",
        blank=True, null=True,
    )

    cidade = models.CharField(
        max_length=200,
        blank=True, null=True,
        verbose_name="Cidade",
        help_text="Campo Obrigatório*"
    )

    estado = models.CharField(
        max_length=200,
        blank=True, null=True,
        verbose_name="Estado",
        help_text="Campo Obrigatório*"
    )

    estado_civil = models.ForeignKey(
        EstadoCivil,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Estado Civil",
        help_text="Campo Obrigatório*"
    )

    curriculo = models.FileField(
        verbose_name="Currículo",
        upload_to="curriculos/",
        blank=True, null=True
    )

    foto = models.ImageField(
        verbose_name="Foto",
        upload_to="perfil",
        blank=True
    )

    video = models.FileField(
        verbose_name="Vídeo",
        upload_to="video",
        blank=True
    )

    celular = models.CharField(
        verbose_name="Celular",
        max_length=30,
        blank=True,
        null=True
    )

    telefone = models.CharField(
        verbose_name="Telefone",
        max_length=30,
        blank=True, null=True
    )

    email = models.EmailField(
        verbose_name="E-mail",
        max_length=100,
        blank=True, null=True,
        help_text="Campo Obrigatório*"
    )

    ja_trabalhou = models.CharField(
        verbose_name="Já trabalhou na empresa?",
        max_length=3,
        choices=SIM_NAO_CHOICES,
        blank=True, null=True,
    )

    pretensao_salarial = models.DecimalField(
        verbose_name="Pretensão Salarial",
        max_digits=8,
        decimal_places=2,
        help_text="Campo Obrigatório*",
        blank=True, null=True,
    )

    disponibilidade_viajar = models.CharField(
        verbose_name="Disponibilidade para Viajar?",
        max_length=3,
        choices=SIM_NAO_CHOICES,
        blank=True, null=True,
    )

    quando_trabalhou = models.DateField(
        verbose_name="Quando Trabalhou",
        null=True,
        blank=True
    )

    projeto_trabalhou = models.CharField(
        verbose_name="Projeto",
        max_length=80,
        blank=True,
        null=True
    )

    link_perfil_linkedin = models.CharField(
        verbose_name="Link perfil do Linkedin",
        max_length=80,
        blank=True,
        null=True
    )

    habilidades_tecnicas = models.TextField(
        verbose_name="Habilidades Técnicas",
        blank=True, null=True
    )

    atividades_relevantes1 = models.TextField(
        verbose_name="1 - Descreva as atividades mais relevantes de sua atuação na empresa",
        blank=True, null=True
    )

    atividades_relevantes2 = models.TextField(
        verbose_name="2 - Descreva as atividades mais relevantes de sua atuação na empresa",
        blank=True, null=True
    )

    atividades_relevantes3 = models.TextField(
        verbose_name="3 - Descreva as atividades mais relevantes de sua atuação na empresa",
        blank=True, null=True
    )

    atividades_relevantes4 = models.TextField(
        verbose_name="4 - Descreva as atividades mais relevantes de sua atuação na empresa",
        blank=True, null=True
    )

    atividades_relevantes5 = models.TextField(
        verbose_name="5 - Descreva as atividades mais relevantes de sua atuação na empresa",
        blank=True, null=True
    )

    medicao_quantitativa_atividades_relevantes1 = models.TextField(
        verbose_name="1 - Como você mede ou medirá QUANTITATIVAMENTE cada atividade",
        blank=True, null=True
    )

    medicao_quantitativa_atividades_relevantes2 = models.TextField(
        verbose_name="2 - Como você mede ou medirá QUANTITATIVAMENTE cada atividade",
        blank=True, null=True
    )

    medicao_quantitativa_atividades_relevantes3 = models.TextField(
        verbose_name="3 - Como você mede ou medirá QUANTITATIVAMENTE cada atividade",
        blank=True, null=True
    )

    medicao_quantitativa_atividades_relevantes4 = models.TextField(
        verbose_name="4 - Como você mede ou medirá QUANTITATIVAMENTE cada atividade",
        blank=True, null=True
    )

    medicao_quantitativa_atividades_relevantes5 = models.TextField(
        verbose_name="5 - Como você mede ou medirá QUANTITATIVAMENTE cada atividade",
        blank=True, null=True
    )

    medicao_qualitativa_atividades_relevantes1 = models.TextField(
        verbose_name="1 - Como você mede ou medirá QUALITATIVAMENTE cada atividade",
        blank=True, null=True
    )

    medicao_qualitativa_atividades_relevantes2 = models.TextField(
        verbose_name="2 - Como você mede ou medirá QUALITATIVAMENTE cada atividade",
        blank=True, null=True
    )

    medicao_qualitativa_atividades_relevantes3 = models.TextField(
        verbose_name="3 - Como você mede ou medirá QUALITATIVAMENTE cada atividade",
        blank=True, null=True
    )

    medicao_qualitativa_atividades_relevantes4 = models.TextField(
        verbose_name="4 - Como você mede ou medirá QUALITATIVAMENTE cada atividade",
        blank=True, null=True
    )

    medicao_qualitativa_atividades_relevantes5 = models.TextField(
        verbose_name="5 - Como você mede ou medirá QUALITATIVAMENTE cada atividade",
        blank=True, null=True
    )

    requisitos_tecnicos = models.ManyToManyField(
        RequisitoTecnico,
        verbose_name="Requisitos Técnicos",
        blank=True
    )

    pares_avaliadores = models.ManyToManyField(
        'pessoa.Pessoa',
        verbose_name="Pares Avaliadores",
        blank=True, null=True
    )

    cargo = models.ForeignKey(
        Cargo,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Cargo na Empresa"
    )

    data_contratacao = models.DateField(
        verbose_name="Data de Contratação",
        blank=True, null=True
    )

    matricula = models.CharField(
        max_length=50,
        blank=True, null=True,
        verbose_name="Matrícula"
    )

    chave_integracao = models.CharField(
        max_length=50,
        blank=True, null=True,
        verbose_name="Chave Integração"
    )

    filial = models.ForeignKey(
        Filial,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Filial"
    )

    grupo = models.ForeignKey(
        Grupo,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        verbose_name="Grupo"
    )

    aceite_politica_privacidade = models.BooleanField(
        verbose_name="Aceite da Política de Privacidade",
        default=False,
        blank=True, null=True
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    gestor = models.ForeignKey(
        User,
        related_name='gestor',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    @property
    def tempo_empresa(self):
        from datetime import date
        hoje = date.today()

        if self.data_contratacao:
            diferenca = hoje - self.data_contratacao
            dias = diferenca.days
            anos, dias = dias // 365, dias % 365
            meses, dias = dias // 30, dias % 30
            return '{} ano(s) e {} mês(es)'.format(
                anos,
                meses
            )
        else:
            return '-'
    

    @property
    def idade(self):
        from datetime import date
        hoje = date.today()

        if self.data_nascimento:
            diferenca = hoje - self.data_nascimento
            dias = diferenca.days
            anos = dias // 365
            return anos
        else:
            return None
    

    @property
    def titulacao(self):
        titulacao = 'Não Informado'
        situacao = ''
        for formacao in self.formacaoacademica_set.all():
            if formacao.nivel_escolaridade == 'Doutorado':
                titulacao = formacao.nivel_escolaridade
                situacao = formacao.get_situacao_display()
            elif formacao.nivel_escolaridade == 'Mestrado' and titulacao not in ('Doutorado'):
                titulacao = formacao.nivel_escolaridade
                situacao = formacao.get_situacao_display()
            elif formacao.nivel_escolaridade == 'Especialização' and titulacao not in ('Doutorado', 'Mestrado'):
                titulacao = formacao.nivel_escolaridade
                situacao = formacao.get_situacao_display()
            elif formacao.nivel_escolaridade == 'Graduação' and titulacao not in ('Doutorado', 'Mestrado', 'Especialização'):
                titulacao = formacao.nivel_escolaridade
                situacao = formacao.get_situacao_display()
            elif formacao.nivel_escolaridade == 'Técnico' and titulacao not in ('Doutorado', 'Mestrado', 'Especialização', 'Graduação'):
                titulacao = formacao.nivel_escolaridade
                situacao = formacao.get_situacao_display()
            elif formacao.nivel_escolaridade == 'Ensino Médio' and titulacao not in ('Doutorado', 'Mestrado', 'Especialização', 'Graduação', 'Técnico'):
                titulacao = formacao.nivel_escolaridade
                situacao = formacao.get_situacao_display()
            elif formacao.nivel_escolaridade == 'Ensino Fundamental' and titulacao not in ('Doutorado', 'Mestrado', 'Especialização', 'Graduação', 'Técnico', 'Ensino Médio'):
                titulacao = formacao.nivel_escolaridade
                situacao = formacao.get_situacao_display()
        
        return "{} {}".format(titulacao, situacao)



    @property
    def is_lider(self):
        if self.user:
            liderados = Pessoa.objects.filter(
                gestor=self.user
            ).count()

            return True if liderados > 0 else False
        else:
            return False
    
    def notas_por_competencia(self):
        from avaliacao_desempenho.models import ItemCompetencia

        Resultado = namedtuple(
            'Resultado', 
            'competencia autoavaliacao gestor pares subordinados total'
        )

        itens_competencia = ItemCompetencia.objects.filter(
            avaliacao_desempenho__pessoa=self,
            avaliacao_desempenho__respondida=True
        )
        
        competencias = [item.competencia for item in itens_competencia]
        competencias = list(set(competencias))

        resultado = []

        for competencia in competencias:
            itens_totais = itens_competencia.filter(
                competencia=competencia,
                avaliacao_desempenho__tipo_avaliacao__in=('autoavaliacao', 'subordinado', 'gestor', 'par')
            )
            media_total = itens_totais.aggregate(Avg('nota'))['nota__avg']

            itens_autoavaliacao = itens_totais.filter(avaliacao_desempenho__tipo_avaliacao='autoavaliacao')
            media_autoavaliacao = itens_autoavaliacao.aggregate(Avg('nota'))['nota__avg']

            itens_gestor = itens_totais.filter(avaliacao_desempenho__tipo_avaliacao='subordinado')
            media_gestor = itens_gestor.aggregate(Avg('nota'))['nota__avg']

            itens_subordinado = itens_totais.filter(avaliacao_desempenho__tipo_avaliacao='gestor')
            media_subordinados = itens_subordinado.aggregate(Avg('nota'))['nota__avg']

            itens_par = itens_totais.filter(avaliacao_desempenho__tipo_avaliacao='par')
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

        return resultado

    def email_boas_vindas(self):
        html_text = render_to_string('pessoas/email_boas_vindas.html')
        text = strip_tags(html_text)

        email = EmailMessage(
            'Cadastro efetuado com sucesso!', text, config('EMAIL_HOST_USER'),
            [self.email])

        email.send()
    
    def save(self, *args, **kwargs):
        if self.pk:
            # If self.pk is not None then it's an update.
            cls = self.__class__
            old = cls.objects.get(pk=self.pk)
            # This will get the current model state since super().save() isn't called yet.
            new = self  # This gets the newly instantiated Mode object with the new values.
            changed_fields = []
            for field in cls._meta.get_fields():
                field_name = field.name
                try:
                    if getattr(old, field_name) != getattr(new, field_name):
                        changed_fields.append(field_name)
                except Exception as ex:  # Catch field does not exist exception
                    pass
            kwargs['update_fields'] = changed_fields
        super().save(*args, **kwargs)

    @property
    def nome_abreviado(self):
        return self.abrevia_nome(self.nome, retira_conectores=True, abrevia_primeiro_nome=False)

    def abrevia_nome(self,nome,
                 abrevia_primeiro_nome=None,
                 retira_conectores=None,
                 abrevia_maria=None,
                 abrevia_depois_de_maria=None,
                 anexa_nome_descendente=None,
                 retira_nome_descendente=None):

        """Abrevia um nome proprio, colocando o ultimo nome no inicio.
        Por padrao, a regra de abreviacao eh:
            - mantem o ultimo nome
            - abrevia todos os outros nomes maiores de 2 caracteres.
            - retira conectores "da", "de", "dos", etc.
        Mas tambem pode:
            - nao abreviar o primeiro nome.
            - abreviar "maria" para "mª" se for o primeiro nome.
            - nao abreviar o nome depois de "maria", qdo "maria" for o primeiro
            nome.
            - anexar nome de descendente ao nome anterior: "junior", "filho",
                "neto", etc.
            - retirar o nome de descendente.
        """

        if abrevia_maria is None:
            abrevia_maria = False
        if abrevia_depois_de_maria is None:
            abrevia_depois_de_maria = True
        if abrevia_primeiro_nome is None:
            abrevia_primeiro_nome = True
        if retira_conectores is None:
            retira_conectores = True
        if anexa_nome_descendente is None:
            anexa_nome_descendente = False
        if retira_nome_descendente is None:
            retira_nome_descendente = False

        if not abrevia_primeiro_nome and abrevia_maria:
            raise ValueError(
                "abrevia_primeiro_nome nao pode ser False quando abrevia_maria "
                "for True.")

        if anexa_nome_descendente and retira_nome_descendente:
            raise ValueError(
                "anexa_nome_descendente e retira_nome_descendente nao "
                "podem ser True ao mesmo tempo.")
        elif anexa_nome_descendente or retira_nome_descendente:
            descendentes = "filha filho junior neta neto".split()

        partes = nome.replace(".", ". ").split()

        if retira_nome_descendente:
            if partes[-1].lower() in descendentes:
                # apaga o nome do descendente
                del partes[-1]
        elif anexa_nome_descendente:
            # anexa o nome de descendente com o nome que vem antes dele.
            # Exemplo: "pedro ferreira junior" seria abreviado para
            # "junior, p. f.", por padrao.
            # Mas se anexa_nome_descendente == True, fica assim:
            # "ferreira junior, p."
            if partes[-1].lower() in descendentes:
                if len(partes) > 2:
                    # soh junta se tiver mais de 2 nomes pq nomes como
                    # "Carlos Neto" ficariam soh com 1 parte e seriam
                    # descartados no teste de um nome soh, abaixo.
                    partes[-2] = " ".join(partes[-2:])
                    del partes[-1]
            else:
                return nome

        if len(partes) == 1:
            # nao abrevia se tem um nome soh.
            return nome

        # a eh o array com nomes que serao abreviados.
        # Nao pega o ultimo nome pq ele nao eh abreviado nunca.
        a = partes[:-1]

        if retira_conectores:
            conectores = "da de do das dos e".split()
            a = [s for s in a if s not in conectores]

        depois_de_maria = None
        if not abrevia_depois_de_maria and a[0].lower() == "maria":
            try:
                depois_de_maria = a[1]
            except IndexError:
                # Quando so existe um nome depois de "maria".
                # Exemplo: maria silva.
                depois_de_maria = None

        # So abrevia palavras com +2 letras.
        # Obs.: partes do nome com 1 letra tambem sao "abreviadas"
        a = [s if len(s) == 2 else s[0] + "." for s in a]

        if depois_de_maria:
            # desfaz abreviacao do nome depois de "maria"
            a[1] = depois_de_maria

        if not abrevia_primeiro_nome:
            # desfaz abreviacao do primeiro nome
            a[0] = partes[0]

        if abrevia_maria and partes[0].lower() == "maria":
            # "maria" vira "mª"
            a[0] = partes[0][0] + "ª"

        return "%s %s" % (" ".join(a), partes[-1])


    def abrevia_de_todas_as_formas(nome):
        """abrevia nomes usando todas as combinacoes possiveis de parametros.
        """

        nomes = []
        bools = [True, False]
        params = {}
        for params['abrevia_primeiro_nome'] in bools:
            for params['retira_conectores'] in bools:
                for params['abrevia_maria'] in bools:
                    for params['abrevia_depois_de_maria'] in bools:
                        for params['anexa_nome_descendente'] in bools:
                            for params['retira_nome_descendente'] in bools:
                                if (params['anexa_nome_descendente'] and
                                        params['retira_nome_descendente']):
                                    continue
                                elif (not params['abrevia_primeiro_nome'] and
                                        params['abrevia_maria']):
                                    continue

                                resultado = abrevia_nome(nome, **params)
                                if resultado != nome:
                                    nomes.append(resultado)
        return list(set(nomes))

    def __str__(self):
        return self.nome

    class Meta:
        app_label = "pessoa"
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        ordering = ["nome"]
