function requisitosController() {
  return {
    toggleSelected(cardElement) {
      var card = $(cardElement),
        isSelected = card[0].hasAttribute('data-selected')

      if (isSelected) {
        $(card).removeAttr('data-selected')
      } else {
        $(card).attr('data-selected', true)
      }
    },

    submit() {

      var data = {
        habilidades: [],
        outras: ""
      }

      $(".card-requisito").each(function () {
        if ($(this)[0].hasAttribute('data-selected')) {
          var id = $(this).attr('data-id'),
            name = $(this).find('.card-right').text()

          data.habilidades.push(Number(id))
        }
      })

      data.outras = $("#habilidades").val()

      $forms.prepareRequest('/pessoas/' + idPessoa + '/', {
        requisitos_tecnicos: data.habilidades,
        habilidades_tecnicas: data.outras
      }, 'PATCH', true).then(function(){
        swal("Sucesso", "Os dados foram salvos", "success").then(function(){
          location.reload()
        })
      }).catch(function(){
        swal("Erro", "Ocorreu um erro, fale com o Administrador", "error")
      })


    }
  }
}