from django.apps import AppConfig


class PerfilConfig(AppConfig):
    name = 'perfil'
    verbose_name = 'Vagas e Análise de Talentos'

    def ready(self):
        import perfil.signals
