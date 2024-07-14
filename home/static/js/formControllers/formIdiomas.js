function idiomasController() {
  return {
    // Clone do form para posteriomente adicionar outros
    base: null,

    // ìndice do ultimo formulário adicionado
    lastFormIndex: Number($('#formIdiomas').find('.fields-container').last().attr('data-index')),

    // Inicia o formulário
    init() {
      this.base = $forms.getFormBase($('#formIdiomas')).clone()
    },

    // Adicionar um novo Idioma
    new() {
      $forms.cloneForm('formIdiomas', ++this.lastFormIndex)
    },

    // Array de Mídias adicionadas
    medias: [],

    // Insere uma nova mídia no form
    insertMedia(data, mediaIndex) {

      // Exibe o Alert
      $forms.showAlert(data, 'formIdiomas', mediaIndex)
      $forms.disableMediaButtons('formIdiomas', mediaIndex)

      var ctx = this;

      // Convert a foto pra base64 e adiciona nos atributos
      $forms.convertToBase64(data.foto).then(function (r) {
        $forms.addMediaAttr('formIdiomas', mediaIndex, r.foto);

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
          $forms.addMediaAttr('formIdiomas', mediaIndex, r.foto);
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

      $forms.showAlert(data, 'formIdiomas', mediaIndex)

    },

    // Apagar a mídia
    removeMedia(formIndex) {
      // Apaga o alert
      $forms.hideAlert("formIdiomas", formIndex)
      $forms.enableMediaButtons("formIdiomas", formIndex)

      // Apaga a mídia
      $forms.prepareRequest('/idiomas/' + formIndex + '/certificado/', null, 'DELETE')
        .then(function () {
          $("#formIdiomas .fields-container[data-index='" + mediaIndex + "']").removeAttr('data-midia')
        })

      // Apagar da Array de Mídias
      this.medias = this.medias.filter(function (m) {
        return m.mediaIndex != formIndex
      })

    },

    // Envia os idiomas
    submit() {

      var allMidias = this.medias;

      var dataArr = []

      // Pega os dados dos campos
      $(".fields-container").each(function () {
        var data = $forms.serializeFieldContainer(this),
          formIndex = $(this).attr('data-index')
        attrMidia = $(this).attr('data-midia'),
          isNewData = $(this).attr('data-new-form') ? true : false

        data.isNewData = isNewData;
        data.formIndex = formIndex;

        // Pega a mídia
        var midia = allMidias.find(function (midia) {
          return midia.mediaIndex == formIndex
        })

        // Insere a mídia se existir
        if (midia) {
          data.midia = midia;

          delete data.midia.foto;
        }

        if (attrMidia && attrMidia.indexOf('base64') != -1) {
          data.certificado = attrMidia;
        }

        // Insere na Array de objetos
        dataArr.push(data)
      })

      $forms.setLoading(true)

      var requestPromises = []

      dataArr.forEach(function (idiomas) {

        var reqType = idiomas.isNewData ? 'POST' : 'PUT'

        if (reqType == "POST") {
          requestPromises.push(
            $forms.prepareRequest('/idiomas/', idiomas, reqType)
          )
        } else {
          requestPromises.push(
            $forms.prepareRequest('/idiomas/' + idiomas.formIndex + '/', idiomas, reqType)
          )
        }
      })

      Promise.all(requestPromises)
        .then(function () {
          swal("Sucesso", "Os dados foram salvos", "success").then(function(){
            location.reload()
          })
          $(".fields-container").removeAttr('data-new-form')
        })
        .catch(function (err) {
          $forms.showErrorAlert(err)
        })
        .finally(function () {
          $forms.setLoading(false)
        })
    },

    remove(id, newForm) {

      if (newForm) return 

      $forms.prepareRequest('/idiomas/' + id + '/', null, 'DELETE')
    }
  }
}