var $forms = {

  // Mudar o form ativo
  changeForm(formID) {
    $(".main-form").addClass('d-none')
    $("form[data-form-id=" + formID + "]").removeClass('d-none')
  },

  // Clonar o formulário
  cloneForm(formId, index) {
    // Pega o último índice do formulário
    var baseForm = this[formId].base.clone(),
      formContent = $('#' + formId + ' .form-content').first();

    baseForm.attr('data-index', index);
    baseForm.attr('data-new-form', "true")
    baseForm.removeAttr('data-midia')
    baseForm.find("select").val("")
    baseForm.find("input[type=checkbox]").removeAttr('checked')
    baseForm.find(".select-outro input").addClass('no-validate')

    // Adicionar ao DOM
    formContent
      // .append("<hr class='mt-5 mb-5'>")
      .append(baseForm)

    // Dá um reset nas actions, sendo atribuída também aos novos elementos 
    addActions()

  },

  // Mostra o alert de mídias
  showAlert(data, formId, mediaIndex) {

    var alert;

    if (formId != "formExperiencia") {
      alert = $("#" + formId + " [data-index='" + mediaIndex + "']")
        .find('.alert');
    } else {
      var container = $(".midia-container[data-id-midia='" + mediaIndex + "']")
      alert = container.find('.alert');
    }

    alert.find('.media-title').text(data.titulo)
    alert.find('.media-description').text(data.descricao)
    alert.find('.media-date').text(data.dataInsercao.toLocaleDateString())
    alert.removeClass('d-none')
  },

  // Esconde o alert
  hideAlert(formId, mediaIndex) {

    var alert;

    if (formId != "formExperiencia") {
      alert = $("#" + formId + " [data-index='" + mediaIndex + "']")
        .find('.alert');
    } else {
      var container = $(".midia-container[data-id-midia='" + mediaIndex + "']")
      alert = container.find('.alert');
    }

    alert.addClass('d-none')
  },

  // Mostra a Input de Link
  showLinkField(formId, mediaIndex) {

    if (formId != "formExperiencia") {
      $("#" + formId).find("[data-index='" + mediaIndex + "']")
        .find('.media-link').removeClass('d-none')
    } else {
      var container = $(".midia-container[data-id-midia='" + mediaIndex + "']")
      container.find('.media-link').removeClass('d-none')
    }

  },

  // Esconde a input de mídia
  hideLinkField(formId, mediaIndex) {

    if (formId != "formExperiencia") {
      $("#" + formId).find("[data-index='" + mediaIndex + "']")
        .find('.media-link').addClass('d-none')
    } else {
      var container = $(".midia-container[data-id-midia='" + mediaIndex + "']")
      container.find('.media-link').addClass('d-none')
    }

  },

  // Desabilita os botões de mídia
  disableMediaButtons(formId, mediaIndex) {


    if (formId != "formExperiencia") {
      $("#" + formId).find("[data-index='" + mediaIndex + "']")
        .find('.media-container .btn').addClass('disabled')
    } else {
      $(".midia-container[data-id-midia='" + mediaIndex + "']")
        .find('.btn').addClass('disabled')
    }


  },

  // habilita os botões de mídia
  enableMediaButtons(formId, mediaIndex) {

    if (formId != "formExperiencia") {
      $("#" + formId).find("[data-index='" + mediaIndex + "']")
        .find('.media-container button').removeClass('disabled')
    } else {
      $(".midia-container[data-id-midia='" + mediaIndex + "']")
        .find('button').removeClass('disabled')
    }


  },

  // Adiciona o atributo da mídia no form
  addMediaAttr(formId, mediaIndex, base64Image) {
    if (formId != "formExperiencia") {
      $("#" + formId).find("[data-index='" + mediaIndex + "']")
        .attr('data-midia', base64Image)
    } else {
      $(".midia-container[data-id-midia='" + mediaIndex + "']")
        .attr('data-midia', base64Image)
    }
  },

  // Pega os dados dentro de uma DIV
  serializeFieldContainer(fieldContainer) {
    var fields = $(fieldContainer).find('[name]'),
      data = {}

    for (field of fields) {
      var field = $(field),
        fieldName = field.attr('name'),
        fieldType = field.attr('type'),
        fieldValue = field.val();
        
      data[fieldName] = fieldValue

      if(fieldType == 'checkbox'){
        data[fieldName] = field.prop('checked')
      }

    }

    return data
  },

  // Converte imagem pra base64
  convertToBase64(file, mediaIndex) {

    if (typeof file != String) {
      return new Promise(function (resolve, reject) {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = function () {
          resolve({
            foto: reader.result,
            formIndex: mediaIndex
          })
        };
        reader.onerror = function (error) {
          resolve({
            error: error,
            formIndex: mediaIndex
          })
        };
      });
    } else {
      return file;
    }
  },

  // Clona o formulário
  getFormBase(form) {
    var formClone = $(form).find('.fields-container').last().clone();
    $(formClone).find('input, select').val("")
    $(formClone).find('.alert').addClass('d-none')
    $(formClone).find('.btn').removeClass('disabled')
    return formClone
  },

  // Candidato / Funcionário
  formFormacaoAcademica: formacoesController(),
  formCursos: cursosController(),
  formIdiomas: idiomasController(),
  formExperiencia: experienciasController(),
  formRequisitos: requisitosController(),
  formTeste: testeController(),

  // Avaliação
  formAvaliacaoMetas: avaliacaoMetasController(),

  // Remove o form e o ht acima dele
  removeForm(btnElement) {
    $(btnElement).parent().prev('hr').remove()
    $(btnElement).parent().remove()

    var formName = $(".data-form-container").attr('id'),
      formIndex = $(btnElement).parent().attr('data-index')
      newForm = $(btnElement).parent().attr('data-new-form') == "true" ? true : false

    $forms[formName].remove(formIndex, newForm)

  },

  setLoading(isLoading, text){
    if(isLoading){
      $(".btn-avancar").css({
        opacity: '.5',
        pointerEvents: 'none'
      }).html("<i class='fa fa-spinner fa-spin'></i> Salvando alterações...")
    } else {
      $(".btn-avancar").css({
        opacity: '1',
        pointerEvents: 'initial'
      }).html(text || "Salvar")
    }
  },

  getDataFromButton(buttonElement){
    var container, formId, mediaIndex

    if ($(buttonElement).hasClass('btn-experiencia')) {
      container = $(buttonElement).parents('.midia-container')
      mediaIndex = container.attr('data-id-midia')
    } else {
      container = $(buttonElement).parents('.fields-container')
      mediaIndex = container.attr('data-index')
    }
    
    formId = container.parents('.data-form-container').attr('id')
    
    var data = {
      foto: container.attr('data-midia'),
      formId: formId,
      mediaIndex: mediaIndex
    }

    if ($(buttonElement).hasClass('btn-experiencia')) {
      var alertContainer = $(buttonElement).parents('.midia-container').find('.alert')
      data.titulo = alertContainer.find('.media-title').text(),
      data.descricao = alertContainer.find('.media-description').text()
    }

    return data;
  },

  prepareRequest(url, data, type, isJSON = false){
    return new Promise(function(resolve, reject){
      $.ajax({
        url: '/api' + url,
        data: isJSON ? JSON.stringify(data) : data,
        type: type,
        contentType: isJSON ? 'application/json' : 'application/x-www-form-urlencoded; charset=UTF-8',
        success: function(res){
          resolve(res)
        },
        error: function(res){
          reject(res)
        }
      })
    })
  },

  showErrorAlert(err){

    let message = "Ocorreu um erro ao salvar as informações: "

    if(err.responseJSON){
      message += "\n"

      var errors = err.responseJSON

      for(errorKey in errors){
        var errContent = errors[errorKey];

        message += "\n\n" + errorKey.toString().charAt(0).toUpperCase() + errorKey.substring(1) + ":"

        errContent.forEach(function(errorMessage){
          message += "\n • " + errorMessage
        })

      }

      swal({
        title: "Erro",
        text: message,
        icon: "error",
      })

    } else {

      swal({
        title: "Erro",
        text: "Ocorreu um erro desconhecido, fale com o Administrador",
        icon: "error",
      })

    }


  }

}

// Candidato
$forms.formCursos.init();
$forms.formFormacaoAcademica.init();
$forms.formExperiencia.init();
$forms.formIdiomas.init();

// Avaliação
$forms.formAvaliacaoMetas.init();