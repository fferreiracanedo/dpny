from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import home
from .views import dados
from .views import perfis
from .views import analises
from .views import correlacionar
from .views import teste_psicologico
from .views import trilha
from .views import treinamento
from .views import experiencia_profissional
from .views import excluir_experiencia_profissional
from .views import formacao_academica
from .views import excluir_formacao_academica
from .views import cursos
from .views import excluir_curso
from .views import idiomas
from .views import excluir_idioma
from .views import excluir_certificado_idioma
from .views import requisitos_tecnicos
from .views import excluir_midia
from .views import excluir_certificado_curso
from .views import excluir_certificado_formacao_academica
from .views import curriculo
from .views import respostas
from .views import ranking
from .views import avaliacoes
from .views import avaliacoes_dashboard
from .views import avaliacao
from .views import potencial
from .views import comite
from .views import resultado_avaliacao
from .views import resultado_equipe
from .views import resultado_avaliacao_individual
from .views import PdiUpdateView
from .views import visualizar_pdi

urlpatterns = [
    path('', dados, name="dados"),
    path('experiencia_profissional/', experiencia_profissional, name="experiencia_profissional"),
    path('excluir_experiencia_profissional/', excluir_experiencia_profissional, name="excluir_experiencia_profissional"),
    path('formacao_academica/', formacao_academica, name="formacao_academica"),
    path('excluir_formacao_academica/', excluir_formacao_academica, name="excluir_formacao_academica"),
    path('excluir_certificado_formacao_academica/', excluir_certificado_formacao_academica, name="excluir_certificado_formacao_academica"),
    path('cursos/', cursos, name="cursos"),
    path('excluir_curso/', excluir_curso, name="excluir_curso"),
    path('excluir_certificado_curso/', excluir_certificado_curso, name="excluir_certificado_curso"),
    path('idiomas/', idiomas, name="idiomas"),
    path('excluir_idioma/', excluir_idioma, name="excluir_idioma"),
    path('excluir_certificado_idioma/', excluir_certificado_idioma, name="excluir_certificado_idioma"),
    path('requisitos_tecnicos/', requisitos_tecnicos, name="requisitos_tecnicos"),
    path('excluir_midia/', excluir_midia, name="excluir_midia"),
    path('perfis/', perfis, name="perfis"),
    path('analises/', analises, name="analises"),
    path('correlacionar/<int:perfil>', correlacionar, name="correlacionar"),
    path('teste_escrito/', teste_psicologico, name="teste_psicologico"),
    path('trilha/', trilha, name="trilha"),
    path('treinamento/<int:treinamento>', treinamento, name="treinamento"),
    path('curriculo/<int:pessoa>', curriculo, name="curriculo"),
    path('respostas/<int:teste_escrito>', respostas, name="respostas"),
    path('ranking/<int:perfil>', ranking, name="ranking"),
    path('avaliacoes/', avaliacoes_dashboard, name="avaliacoes_dashboard"),
    path('potencial/', potencial, name="potencial"),
    path('comite/', comite, name="comite"),
    path('avaliacoes/<slug:tipo>', avaliacoes, name="avaliacoes"),
    path('avaliacoes/<int:avaliacao>/<slug:tipo>', avaliacao, name="avaliacao"),
    path('avaliacoes_resultado/', resultado_avaliacao, name="resultado_avaliacao"),
    path('avaliacoes_resultado_individual/<int:id_pessoa>', resultado_avaliacao_individual, name="resultado_avaliacao_individual"),
    path('resultado_equipe/', resultado_equipe, name="resultado_equipe"),
    path('pdi/', login_required(PdiUpdateView.as_view(template_name='pdi_form.html')), name="atualizar_pdi"),
    path('pdi/<int:id_pessoa>', visualizar_pdi, name="visualizar_pdi"),
    path('', include('django.contrib.auth.urls')),
]