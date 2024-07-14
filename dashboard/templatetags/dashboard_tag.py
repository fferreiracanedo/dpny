from django import template

register = template.Library()


@register.simple_tag
def resposta_potencial(resposta):
    OPCOES_RESPOSTA_POTENCIAL = {
        'NA': 'Avaliação não apropriada no momento (menos de 6 meses na empresa)',
        'R-': 'Não satisfatório, devendo ser fruto de análise para atividade de menor complexidade ou desligamento',
        'R': 'Situação estável',
        'R+': 'Capacidade para crescimento horizontal, atividades mais complexas',
        'AP': 'Potencial para crescimento vertical',

    }

    return OPCOES_RESPOSTA_POTENCIAL[resposta] if resposta else ''


@register.filter
def porcentagem(parte, inteiro):
    try:
        return "%d%%" % (float(parte) / inteiro * 100)
    except (ValueError, ZeroDivisionError):
        return ""