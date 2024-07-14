from django.apps import AppConfig


class AvaliacaoDesempenhoConfig(AppConfig):
    name = 'avaliacao_desempenho'
    verbose_name = 'Avaliação de Desempenho'

    def ready(self):
        import avaliacao_desempenho.signals
