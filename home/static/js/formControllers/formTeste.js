function testeController() {
  return {
    medias: [],

    insertMedia(data, mediaIndex) {
      // Exibe o Alert
      var container = $(".midia-container[data-id-midia='" + mediaIndex + "']")

      $forms.showAlert(data, 'formExperiencia', mediaIndex)
      $forms.hideLinkField('formExperiencia', mediaIndex)
      $forms.disableMediaButtons('formExperiencia', mediaIndex)

      var ctx = this;

      // Convert a foto pra base64 e adiciona nos atributos
      $forms.convertToBase64(data.foto).then(function (r) {

        $forms.addMediaAttr('formExperiencia', mediaIndex, r.foto);

        // Adicionar na array de mídias
        data.mediaIndex = mediaIndex

        data.foto = r.foto
        ctx.medias.push(data)
      })

    },

    editMedia(data, mediaIndex) {
      // Procura a mídia na array
      var arrMediaIndex = this.medias.findIndex(function (m) {
        return m.mediaIndex == mediaIndex
      })

      // Convert a foto pra base64 e adiciona nos atributos

      if (arrMediaIndex == -1) {
        arrMediaIndex = this.medias.push()
      }

      if (data.foto) {
        $forms.convertToBase64(data.foto).then(function (r) {
          $forms.addMediaAttr('formExperiencia', mediaIndex, r.foto);
          // Edita a mídia na array
          data.foto = r.foto
        })
      } else {
        var mediaObj = this.medias[arrMediaIndex]
        if (mediaObj) {
          data.foto = mediaObj.foto
        }
      }

      data.mediaIndex = mediaIndex
      this.medias[arrMediaIndex] = data

      $forms.showAlert(data, 'formExperiencia', mediaIndex)

    },


    // Apagar a mídia
    removeMedia(mediaIndex) {

      // Apaga o alert
      $(".midia-container[data-id-midia='" + mediaIndex + "'] .alert").addClass('d-none')

      $forms.enableMediaButtons("formExperiencia", mediaIndex)

      // // Apaga a mídia
      // $forms.prepareRequest('/midias/' + mediaIndex, null, 'DELETE')

      // Apagar da Array de Mídias
      this.medias = this.medias.filter(function (m) {
        return m.mediaIndex != mediaIndex
      })

    },

    // Envia as Formações Acadêmicas
    submit() {
      var dataArr = []

      $(".fields-container").each(function () {
        var data = $forms.serializeFieldContainer(this),
          afirmativa = $(this).attr('data-id-afirmativa')
        attrMidia = $(this).find('.midia-container').attr('data-midia'),
        idTeste = $(this).attr('data-id-teste'),

        data.afirmativa = Number(afirmativa)
        data.teste_psicologico = Number(idTeste)

        if(attrMidia){
          data.midia = attrMidia;
        }

        // Insere na Array de objetos
        dataArr.push(data)
      })

      $forms.setLoading(true)

      var promises = []

      dataArr.forEach(function(data){
        promises.push($forms.prepareRequest('/respostas/', data, 'POST'))
      })

      Promise.all(promises)
      .then(function(){
        $forms.setLoading(false)
        swal("Enviadas", "Suas respostas foram enviadas com sucesso!", "success")
        .then(function(){
          location.reload()
        })
      })
      .catch(function(){
        swal("Erro", "Ocorreu um erro, fale com o Administrador", "error")
      })

    },

  }
}