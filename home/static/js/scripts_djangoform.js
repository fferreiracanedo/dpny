document.getElementById("id_user").style.display = "none";
maximo_essencia_talento = 5;

document.getElementById("id_comunicacao").onchange = function(){
    if (verificar_marcacao_essencia() > maximo_essencia_talento){
        document.getElementById("id_comunicacao").checked = false;
    }
}

document.getElementById("id_negociacao").onchange = function(){
    if (verificar_marcacao_essencia() > maximo_essencia_talento){
        document.getElementById("id_negociacao").checked = false;
    }
}

document.getElementById("id_comportamento").onchange = function(){
    if (verificar_marcacao_essencia() > maximo_essencia_talento){
        document.getElementById("id_comportamento").checked = false;
    }
}

document.getElementById("id_competitividade").onchange = function(){
    if (verificar_marcacao_essencia() > maximo_essencia_talento){
        document.getElementById("id_competitividade").checked = false;
    }
}

document.getElementById("id_criatividade").onchange = function(){
    if (verificar_marcacao_essencia() > maximo_essencia_talento){
        document.getElementById("id_criatividade").checked = false;
    }
}

document.getElementById("id_inovacao").onchange = function(){
    if (verificar_marcacao_essencia() > maximo_essencia_talento){
        document.getElementById("id_inovacao").checked = false;
    }
}

document.getElementById("id_protagonismo").onchange = function(){
    if (verificar_marcacao_essencia() > maximo_essencia_talento){
        document.getElementById("id_protagonismo").checked = false;
    }
}

document.getElementById("id_equilibrio_emocional").onchange = function(){
    if (verificar_marcacao_essencia() > maximo_essencia_talento){
        document.getElementById("id_equilibrio_emocional").checked = false;
    }
}

document.getElementById("id_solucao_problemas").onchange = function(){
    if (verificar_marcacao_essencia() > maximo_essencia_talento){
        document.getElementById("id_solucao_problemas").checked = false;
    }
}

document.getElementById("id_etica").onchange = function(){
    if (verificar_marcacao_essencia() > maximo_essencia_talento){
        document.getElementById("id_etica").checked = false;
    }
}

function verificar_marcacao_essencia(){
    quantidade = 0;

    if (document.getElementById("id_comunicacao").checked == true){
        quantidade++;
    }

    if (document.getElementById("id_negociacao").checked == true){
        quantidade++;
    }

    if (document.getElementById("id_comportamento").checked == true){
        quantidade++;
    }

    if (document.getElementById("id_competitividade").checked == true){
        quantidade++;
    }

    if (document.getElementById("id_criatividade").checked == true){
        quantidade++;
    }

    if (document.getElementById("id_inovacao").checked == true){
        quantidade++;
    }

    if (document.getElementById("id_protagonismo").checked == true){
        quantidade++;
    }

    if (document.getElementById("id_equilibrio_emocional").checked == true){
        quantidade++;
    }

    if (document.getElementById("id_solucao_problemas").checked == true){
        quantidade++;
    }

    if (document.getElementById("id_etica").checked == true){
        quantidade++;
    }

    return quantidade;
}

document.getElementById("id_gestao_negocio").onchange = function(){
    if (verificar_marcacao_talento() > maximo_essencia_talento){
        document.getElementById("id_gestao_negocio").checked = false;
    }
}

document.getElementById("id_gestao_pessoas").onchange = function(){
    if (verificar_marcacao_talento() > maximo_essencia_talento){
        document.getElementById("id_gestao_pessoas").checked = false;
    }
}

document.getElementById("id_tomada_decisao").onchange = function(){
    if (verificar_marcacao_talento() > maximo_essencia_talento){
        document.getElementById("id_tomada_decisao").checked = false;
    }
}

document.getElementById("id_accontability").onchange = function(){
    if (verificar_marcacao_talento() > maximo_essencia_talento){
        document.getElementById("id_accontability").checked = false;
    }
}

document.getElementById("id_excelencia_operacional").onchange = function(){
    if (verificar_marcacao_talento() > maximo_essencia_talento){
        document.getElementById("id_excelencia_operacional").checked = false;
    }
}

document.getElementById("id_atendimento_cliente").onchange = function(){
    if (verificar_marcacao_talento() > maximo_essencia_talento){
        document.getElementById("id_atendimento_cliente").checked = false;
    }
}

document.getElementById("id_relacionamento_interpessoal").onchange = function(){
    if (verificar_marcacao_talento() > maximo_essencia_talento){
        document.getElementById("id_relacionamento_interpessoal").checked = false;
    }
}

document.getElementById("id_trabalho_equipe").onchange = function(){
    if (verificar_marcacao_talento() > maximo_essencia_talento){
        document.getElementById("id_trabalho_equipe").checked = false;
    }
}

document.getElementById("id_aprendizado_desenvolvimento").onchange = function(){
    if (verificar_marcacao_talento() > maximo_essencia_talento){
        document.getElementById("id_aprendizado_desenvolvimento").checked = false;
    }
}

document.getElementById("id_gestao_mudanca").onchange = function(){
    if (verificar_marcacao_talento() > maximo_essencia_talento){
        document.getElementById("id_gestao_mudanca").checked = false;
    }
}

function verificar_marcacao_talento(){
    quantidade = 0;

    if (document.getElementById("id_gestao_negocio").checked == true){
        quantidade++;
    }

    if (document.getElementById("id_gestao_pessoas").checked == true){
        quantidade++;
    }

    if (document.getElementById("id_tomada_decisao").checked == true){
        quantidade++;
    }

    if (document.getElementById("id_accontability").checked == true){
        quantidade++;
    }

    if (document.getElementById("id_excelencia_operacional").checked == true){
        quantidade++;
    }

    if (document.getElementById("id_atendimento_cliente").checked == true){
        quantidade++;
    }

    if (document.getElementById("id_relacionamento_interpessoal").checked == true){
        quantidade++;
    }

    if (document.getElementById("id_trabalho_equipe").checked == true){
        quantidade++;
    }

    if (document.getElementById("id_aprendizado_desenvolvimento").checked == true){
        quantidade++;
    }

    if (document.getElementById("id_gestao_mudanca").checked == true){
        quantidade++;
    }

    return quantidade;
}