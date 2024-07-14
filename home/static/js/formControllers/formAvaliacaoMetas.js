function avaliacaoMetasController() {
  return {
    base: null,

    lastFormIndex: Number($('#formAvaliacaoMetas').find('.fields-container').last().attr('data-index')),

    init() {
      this.base = $forms.getFormBase($('#formAvaliacaoMetas')).clone()
    },

    new() {
      $forms.cloneForm('formAvaliacaoMetas', ++this.lastFormIndex)
      $(".fields-container").last().find('.titulo-meta').text("Meta " + (Number(this.lastFormIndex) + 1))
    },

    submit() {

      var promiseMetas = []
      var idAvaliacao = $("#idAvaliacao").val()

      // Iterar as metas
      $('#formAvaliacaoMetas .fields-container').each(function(){
        var dadosMeta = $forms.serializeFieldContainer($(this)),
          isNew = $(this).attr('data-new-form') == "true" ? true : false

        dadosMeta.forma_medicao = "QT"
        dadosMeta.avaliacao_desempenho = idAvaliacao

        // Cria as promises para as metas
        if(isNew){
          // Se for uma nova meta
          promiseMetas.push(
            $forms.prepareRequest('/itens_metas/', dadosMeta, 'POST')
          )
        } else {
          // Se tiver editado a meta
          var idMeta = $(this).attr('data-index')
          promiseMetas.push(
            $forms.prepareRequest('/itens_metas/' + idMeta + '/', dadosMeta, 'PUT')
          )
        }
      })

      Promise.all(promiseMetas)
      .then(function(){
        swal("Sucesso", "As metas foram salvas", "success").then(function(){
          location.reload()
        })
      })
      .catch(function(){
        swal("Erro", "Ocorreu um erro, fale com o Administrador", "error")
      })
    },

    remove(id, isNewForm) { 
      if(isNewForm == false){
        $forms.prepareRequest('/itens_metas/' + id + "/", null, "DELETE")
      }
    }

  }
}