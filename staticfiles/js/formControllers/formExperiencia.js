function experienciasController() {
  return {
    // Clone do form para posteriomente adicionar outros
    base: null,

    // ìndice do ultimo formulário adicionado
    lastFormIndex: Number($('#formExperiencia').find('.fields-container').last().attr('data-index')),

    // Inicia o formulário
    init() {
      this.base = $forms.getFormBase($('#formExperiencia')).clone()
    },

    medias: [],

    // Adicionar uma nova experiência
    new() {
      $forms.cloneForm('formExperiencia', ++this.lastFormIndex)
    },

    newMedia() {
      var mediaContainer = $(".midia-container").last(),
        newMediaContainer = mediaContainer.clone();

      newMediaContainer.find('.alert').addClass('d-none')
      newMediaContainer.find('button').removeClass('disabled')
      newMediaContainer.find('.media-link').addClass('d-none')
      newMediaContainer.find('input').val("")
      newMediaContainer.attr('data-new-media', 'true')

      var lastID = Number(mediaContainer.attr('data-id-midia'))
      newMediaContainer.attr("data-id-midia", lastID + 1)

      $(newMediaContainer).insertAfter(mediaContainer)

      addActions()

    },

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

      // Cria um novo 
      if($('.midia-container').length == 1){
        this.newMedia()
      }

      // Apaga o alert
      $(".midia-container[data-id-midia='" + mediaIndex + "']").remove()

      $forms.enableMediaButtons("formExperiencia", mediaIndex)

      // Apaga a mídia
      $forms.prepareRequest('/midias/' + mediaIndex, null, 'DELETE')

      // Apagar da Array de Mídias
      this.medias = this.medias.filter(function (m) {
        return m.mediaIndex != mediaIndex
      })


    },

    // Envia as Formações Acadêmicas
    submit() {

      validateFields()

      var dataArr = []

      // Pega os dados dos campos
      $(".fields-container").each(function () {
        var data = $forms.serializeFieldContainer(this),
          formIndex = $(this).attr('data-index')
        isNewData = $(this).attr('data-new-form') ? true : false

        
        data.isNewData = isNewData;
        data.formIndex = formIndex;
        
        // Insere na Array de objetos
        dataArr.push(data)
      })

      // Array para as Promisses
      var requestPromises = []

      // Itera todos os dados
      dataArr.forEach(function (experiencia) {

        var reqType = experiencia.isNewData ? 'POST' : 'PUT'

        if (reqType == "POST") {
          requestPromises.push(
            $forms.prepareRequest('/experiencias_profissionais/', experiencia, reqType)
          )
        } else {
          requestPromises.push(
            $forms.prepareRequest('/experiencias_profissionais/' + experiencia.formIndex + '/', experiencia, reqType)
          )
        }
      })

      var links = []
      var allMidias = this.medias;
      var error = false;

      $(".midia-container").each(function () {

        if (error) return false

        var idMidia = $(this).attr('data-id-midia')

        var linkElement = $(this).find('input[name=link]'),
          link = linkElement.val()

        var isNewMedia = $(this).attr('data-new-media') ? true : false

        if (!$(this).find('.media-link').hasClass('d-none')) {
          if (link) {
            links.push({
              mediaIndex: idMidia,
              link: link,
              titulo: "",
              descricao: "",
              dataInsercao: new Date(Date.now()).toISOString().split('T')[0],
              isNewMedia: isNewMedia
            })
          } else {
            $(this).addClass('is-invalid').find('input').focus()
            error = true
          }
        }

      })

      if (error) return

      $forms.setLoading(true)

      allMidias = allMidias.concat(links)

      allMidias.forEach(function (midia) {

        var isNewMedia = midia.isNewMedia

        if(isNewMedia == undefined){
          isNewMedia = false
        }

        midia.arquivo = midia.foto ? midia.foto : null

        if(isNewMedia){
          requestPromises.push(
            $forms.prepareRequest('/midias/', midia, 'POST')
          )
        } else {
          requestPromises.push(
            $forms.prepareRequest('/midias/' + midia.mediaIndex + '/', midia, 'PUT')
            .catch(function(){
              $forms.prepareRequest('/midias/', midia, 'POST')
            })
          )
        }
      })


      // Pegas as respostas das perguntas
      var respostas = $forms.serializeFieldContainer($('.perguntas-experiencia'))

      var promiseRespostas = $forms.prepareRequest('/pessoas/' + idPessoa + '/', respostas, 'PATCH')

      requestPromises.push(promiseRespostas)

      // Faz a Request das Promises
      Promise.all(requestPromises)
        .then(function () {
          swal("Sucesso", "Os dados foram salvos", "success").then(function(){
            location.reload()
          })
          this.medias = []
          $(".fields-container").removeAttr('data-new-form')
          $(".midia-container").removeAttr('data-new-midia')
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

      $forms.prepareRequest('/experiencias_profissionais/' + id + '/', null, 'DELETE')
    }

  }
}