var $mediaModal = {

  droppedImage: null,

  init() {
    var el = $("#modalMedia .form-group").detach()
    $("#modalMedia .modal-title").text("Certificado")

    if (location.href.indexOf('/experiencia_profissional/') != -1) {
      $(el).insertAfter($("#mediaImageThumbnail"))
    }
  },

  // Abre o Modal
  open(formId, mediaIndex) {
    // Adiciona aos atributos
    $("#modalMedia")
      .attr({
        'data-form-id': formId,
        'data-media-index': mediaIndex
      })
      .modal()
  },

  // Fecha o modal
  close() {
    $("#modalMedia").modal('hide')
  },

  // Cria uma preview da imagem
  loadThumbnail(file) {
    var file = file || this.droppedImage || $("#mediaImageFile").prop('files')[0],
      fileReader = new FileReader();

    fileReader.onloadend = function () {
      $("#mediaImageThumbnail").css({
        background: '#d8d8d8 url(' + fileReader.result + ') center center'
      })
      $("#mediaImageThumbnail div, .or-text").css({
        opacity: 0
      })
    }

    if (file) {
      fileReader.readAsDataURL(file)
    }
  },

  // Remove a preview
  removeThumbnail() {
    $("#mediaImageThumbnail").css({
      backgroundImage: 'none'
    })

    $("#mediaImageThumbnail div, .or-text").css({
      opacity: 1
    })
  },

  // Retorna os dados presentes no modal
  getData() {
    var titulo = $("#tituloMidia").val()

    titulo = titulo == undefined ? "Certificado" : titulo
    titulo = titulo == "" ? "Sem título" : titulo

    return {
      titulo: titulo,
      descricao: $("#descricaoMidia").val() || "",
      foto: this.droppedImage || $("#mediaImageFile").prop('files')[0],
      dataInsercao: new Date(Date.now()),
    }
  },

  // Limpa os campos
  clear() {

    this.removeThumbnail()

    $("#mediaImageThumbnail > div, .or-text").css({
      opacity: 1
    })

    this.$droppedImage = null
    $('#modalMedia form').trigger('reset')
  },

  // Carrega os dados da midia
  loadData(data) {

    if(data.titulo != undefined || data.descricao != undefined ){
      $("#tituloMidia").val(data.titulo)
      $("#descricaoMidia").val(data.descricao)
    }

    if(typeof data.foto == "string"){
      $("#mediaImageThumbnail").css({
        background: '#d8d8d8 url(' + data.foto + ') center center'
      })
    } else {
      this.loadThumbnail(data.foto)
    }

  },

  // Altera ou tira o modal de somente leitura
  setReadOnly(isReadOnly) {
    if (isReadOnly) {
      this.setEditMode(false)
      $("#mediaImageThumbnail").css({
        pointerEvents: 'none'
      }).find("div, .or-text").css('opacity', 0)
      $("#modalMedia input, #modalMedia textarea").attr('disabled', 'disabled')
      $("#btnSalvarMidia").addClass('d-none')
      $("#btnApagarMidia").removeClass('d-none')
    } else {
      $("#mediaImageThumbnail").css({
        pointerEvents: 'initial'
      }).find("div, .or-text").css('opacity', 1)
      $("#modalMedia input, #modalMedia textarea").removeAttr('disabled')
      $("#btnSalvarMidia").removeClass('d-none')
      $("#btnApagarMidia").addClass('d-none')
    }
  },

  // Muda para o modo de edição
  setEditMode(isEditMode) {
    if (isEditMode) {
      this.setReadOnly(false)
      $("#btnSalvarMidia").addClass('d-none')
      $("#btnEditarMidia").removeClass('d-none')
      $("#mediaImageThumbnail div, .or-text").css('opacity', 0)
    } else {
      $("#btnSalvarMidia").removeClass('d-none')
      $("#btnEditarMidia").addClass('d-none')
    }
  }

}

$mediaModal.init();
