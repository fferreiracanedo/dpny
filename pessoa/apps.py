from django.apps import AppConfig


class PessoaConfig(AppConfig):
    name = 'pessoa'
    verbose_name = 'Banco de Talentos'

    def ready(self):
        import pessoa.signals
