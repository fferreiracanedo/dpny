"""gestor_rh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from home import urls as home_urls
from dashboard import urls as dashboard_urls

from pessoa.api.viewsets import PessoaViewSet
from pessoa.api.viewsets import ExperienciaProfissionalViewSet
from pessoa.api.viewsets import FilhoViewSet
from pessoa.api.viewsets import FormacaoAcademicaViewSet
from pessoa.api.viewsets import CursoViewSet
from pessoa.api.viewsets import IdiomaViewSet
from pessoa.api.viewsets import MidiaViewSet
from teste_psicologico.api.viewsets import RespostaViewSet
from teste_psicologico.api.viewsets import TestePsicologicoViewSet
from avaliacao_desempenho.api.viewsets import AvaliacaoDesempenhoViewSet
from avaliacao_desempenho.api.viewsets import ItemCompetenciaViewSet
from avaliacao_desempenho.api.viewsets import ItemMetaViewSet
from avaliacao_desempenho.api.viewsets import ItemPotencialViewSet


router = routers.DefaultRouter()
router.register(r'pessoas', PessoaViewSet, base_name='Pessoa')
router.register(r'experiencias_profissionais', ExperienciaProfissionalViewSet, base_name='ExperienciaProfissional')
router.register(r'filhos', FilhoViewSet, base_name='Filho')
router.register(r'formacoes_academicas', FormacaoAcademicaViewSet, base_name='FormacaoAcademica')
router.register(r'cursos', CursoViewSet, base_name='Curso')
router.register(r'idiomas', IdiomaViewSet, base_name='Idioma')
router.register(r'midias', MidiaViewSet, base_name='Midia')
router.register(r'respostas', RespostaViewSet, base_name='Resposta')
router.register(r'testes_psicologicos', TestePsicologicoViewSet, base_name='TestePsicologico')
router.register(r'avaliacoes_desempenhos', AvaliacaoDesempenhoViewSet, base_name='AvaliacaoDesempenho')
router.register(r'itens_competencias', ItemCompetenciaViewSet, base_name='ItemCompetencia')
router.register(r'itens_metas', ItemMetaViewSet, base_name='ItemMeta')
router.register(r'itens_potenciais', ItemPotencialViewSet, base_name='ItemPotencial')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls)),
    path('api/', include(router.urls)),
    path('accounts/', include('allauth.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('examples/', include('outbox_base_layout.urls')),
    path('core/', include('core.urls')),
    path('dashboard', include(dashboard_urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
       
    ] + urlpatterns

admin.site.site_header = "Gestor de RH"
admin.site.index_title = "Sistema de Administração"
admin.site.site_title = "Sistema de Gestão de RH"