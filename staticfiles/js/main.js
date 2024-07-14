
_prod = false

$(window).on('beforeunload', function () {
  if (_prod == true) {
    return confirm("Confirm refresh");
  }
})

var isDeviceIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;

var excludeCustomScrollbar = [
  "/accounts/login/"
]

if(excludeCustomScrollbar.indexOf(document.URL) != -1){
  $('body').css({
    overflow: 'initial'
  })
}

if (isDeviceIOS && excludeCustomScrollbar.indexOf(document.URL) == -1) {
  $(".scrollbar").mCustomScrollbar()
}

// Collapsible
$(".section-selector a[data-sideview]").click(function () {
  var section = $(this).attr('data-sideview')
  $sidebar.setSection(section)
})

// Sidebar
$("#toggleSidebar").click(function () {
  $sidebar.toggle()
})

$("li[data-toggle='collapse']").click(function () {
  var collapse = $(this).find('.collapse'),
    icon = $(this).find('.fa-angle-down');

  if (!collapse.hasClass('show')) {
    icon.css('transform', 'rotate(180deg)')
  } else {
    icon.css('transform', 'rotate(0deg)')
  }

})

$("#sideMenu li").click(function () {
  var to = $(this).attr('data-form-id')
  $forms.changeForm(to)
  $sidebar.setActiveMenuItem(this)
})

$("#userPhotoFile").change(function () {
  var imageFile = $(this)[0].files[0]
  if (imageFile) {
    $sidebar.changeUserPhoto(imageFile)
  }
})

$(".btn-loggout").click(function (e) {
  e.preventDefault()
  var button = $(this)
  swal({
    title: "Sair da conta",
    text: "Todos os dados não salvos serão perdidos",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then(function (sair) {
    if (sair) {
      $.post(button.attr('href'), null, function () {
        location.href = "/accounts/login/"
      })
    }
  })
  return false
})

function validateFields() {
  var error = false

  $('.form-content input, .form-content select, .form-content textarea, .form-content [name]')
    .not("[name=data_termino], input[name=link], .no-validate, input[type=checkbox]").each(function () {
      if (!error) {
        if ($(this).val().length == 0) {
          console.log($(this))
          $(this).addClass('is-invalid').focus()
          error = true
        }
      }
    })

  if (!error) {
    return true
  } else {
    return false
  }

}

$('.btn-submit-idioma').click(function (e) {
  e.preventDefault()

  if (validateFields()) {
    $forms.formIdiomas.submit()
  }

})

$('.btn-submit-formacao').click(function (e) {
  e.preventDefault()

  if (validateFields()) {
    $forms.formFormacaoAcademica.submit()
  }

})

$('.btn-submit-curso').click(function (e) {
  e.preventDefault()

  if (validateFields()) {
    $forms.formCursos.submit()
  }

})

$('.btn-submit-experiencia').click(function (e) {
  e.preventDefault()
  if (validateFields()) {
    $forms.formExperiencia.submit()
  }
})

$('.btn-submit-requisitos').click(function (e) {
  e.preventDefault()
  $forms.formRequisitos.submit()
})

$('.btn-submit-teste').click(function (e) {
  e.preventDefault()
  if (validateFields()) {
    $forms.formTeste.submit()
  }
})

// Botões de adicionar

$("#btnAddFormacao").click(function () {
  $forms.formFormacaoAcademica.new()
})

$("#btnAddCurso").click(function () {
  $forms.formCursos.new()
})

$("#btnAddIdioma").click(function () {
  $forms.formIdiomas.new()
})

$("#btnAddExperiencia").click(function () {
  $forms.formExperiencia.new()
})

$("#btnAddMidiaExperiencia").click(function () {
  $forms.formExperiencia.newMedia()
})


/**
 * FUNÇÃO PARA ATRIBUIR A AÇÃO AOS BOTÕES QUANDO FOREM CRIADOS NOVOS ELEMENTOS
*/

function addActions() {
  $(".btn-carregar").click(function () {
    $mediaModal.setReadOnly(false)
    $mediaModal.setEditMode(false)
    $mediaModal.clear()


    var data = $forms.getDataFromButton($(this))
    $mediaModal.open(data.formId, data.mediaIndex);
  })

  $(".btn-apagar-link").click(function () {

    var button = this;

    swal({
      title: "Apagar mídia",
      text: "Tem certeza que deseja apagar essa mídia?",
      icon: "warning",
      buttons: true,
      dangerMode: true,
    }).then(function (canDelete) {
      if (canDelete) {
        var id = $(button).parents('.midia-container').attr('data-id-midia')
        $forms.formExperiencia.removeMedia(id)
      }
    })
  })

  $(".btn-media-link").click(function () {

    var data = $forms.getDataFromButton($(this))

    $forms.showLinkField(data.formId, data.mediaIndex)
    $forms.hideAlert(data.formId, data.mediaIndex)
  })

  $(".btn-remover").click(function () {
    $forms.removeForm(this)
  })

  $('input, select, textarea').on('keydown change', function () {
    $(this).removeClass('is-invalid')
  })

  // Select Outro em Formação e Cursos
  $(".select-opcao-outro").change(function () {

    var outroContainer = $(this).parents('.fields-container').find('.select-outro')
    var outroField = $(outroContainer).find('input')
    var selectValue = $(this).find('option:selected').text().toLowerCase()

    if (selectValue.indexOf('outro') != -1) {
      outroContainer.removeClass('d-none')
      outroField.removeClass('no-validate')
    } else {
      outroContainer.addClass('d-none')
      outroField.val("")
      outroField.addClass('no-validate')
    }
  })

  // Coloca a Opção "Outro" no SELECT como última opção
  $("select").find('option').each(function(){
    if($(this).text().toLowerCase().includes('outro')){
      var copy = $(this).clone();

      var parent = $(this).parent()
      
      $(this).remove()
      $(parent).append(copy)

    }
  })

  $(".lbl-cargo-atual").click(function(){
    var checkbox = $(this).parent().find('input')
    checkbox.prop('checked', !checkbox.prop('checked'))
  })

  $("select[name='nivel_escolaridade']").change(function(){
    var value = $(this).val()
    var containerCurso = $(this).parents('.fields-container').find('.col-curso')

    // if(value == "Ensino Médio" || value == "Ensino Fundamental"){
    //   containerCurso.addClass('d-none')
    //   containerCurso.find('select').val('').addClass('no-validate')
    // } else {
    //   containerCurso.removeClass('d-none')
    // }

  })

  addMediaActions();
}

addActions();

// Modal

function addMediaActions() {
  $(".btn-see-media").click(function () {
    // Pega o Form correspondente ao boão
    var data = $forms.getDataFromButton($(this))

    $mediaModal.setReadOnly(true)
    $mediaModal.loadData(data)
    $mediaModal.open(data.formId, data.mediaIndex)

  })

  $(".btn-edit-media").click(function () {
    // Pega o Form correspondente ao boão

    var data = $forms.getDataFromButton($(this))

    $mediaModal.setEditMode(true, data.formId, data.mediaIndex)
    $mediaModal.loadData(data)
    $mediaModal.open(data.formId, data.mediaIndex)
  })
}

$("#mediaImageFile").change(function () {

  if (this.files.length == 0) {
    $mediaModal.removeThumbnail()
  } else {
    $mediaModal.droppedImage = false
    $mediaModal.loadThumbnail()
  }

})

function getMediaPropsFromModal(el) {
  if (el) {
    var modalElement = $('#modalMedia'),
      formID = modalElement.attr('data-form-id'),
      mediaIndex = modalElement.attr('data-media-index')

    return {
      formID: formID,
      index: mediaIndex
    }
  }
}

$("#btnSalvarMidia").click(function () {
  // Pega a ID e Índices dos forms
  var mediaProps = getMediaPropsFromModal(this)

  // Verifica se existe foto
  if ($mediaModal.getData().foto == null) {
    swal("Erro", "Selecione uma imagem", "error")
  } else {

    // Adicionar a mídia
    $forms[mediaProps.formID].insertMedia($mediaModal.getData(), mediaProps.index)

    // Limpa e fecha o modal
    $mediaModal.clear();
    $mediaModal.close();
  }

})

$("#btnEditarMidia").click(function () {

  // Verifica se existe foto
  swal({
    title: "Editar mídia",
    text: "Tem certeza que deseja editar essa mídia?",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then(function (canEdit) {
    if (canEdit) {
      // Pega a ID e Índices dos forms
      var mediaProps = getMediaPropsFromModal(this)

      const data = $mediaModal.getData()

      // Edita a mídia
      $forms[mediaProps.formID].editMedia($mediaModal.getData(), mediaProps.index)

      // Limpa e fecha o modal
      $mediaModal.close();
      $mediaModal.clear();

    }
  })

})

$("#btnApagarMidia").click(function () {
  var mediaProps = getMediaPropsFromModal(this)
  swal({
    title: "Apagar mídia",
    text: "Tem certeza que deseja apagar essa mídia?",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then(function (canDelete) {
    if (canDelete) {
      $mediaModal.close()
      $mediaModal.clear()
      $forms[mediaProps.formID].removeMedia(mediaProps.index)
    }
  })
})

// Modal Drag'n Drop

// Desabilita o Drag'n Drop para a página

$("*").on('drag dragstart dragend dragover dragenter dragleave drop', function (e) {
  e.preventDefault();
  e.stopPropagation();
})

$("#mediaImageThumbnail").on('dragenter', function (e) {
  $(this).css({
    opacity: .5
  })
})

$("#mediaImageThumbnail").on('dragleave', function (e) {
  $(this).css({
    opacity: 1
  })
})

$mediaModal.setReadOnly(true)

$("#mediaImageThumbnail").on('drop', function (e) {
  var file = e.originalEvent.dataTransfer.files[0]

  // Verifica se oarquivo é uma imagem
  if (file && file.type.indexOf('image') != -1) {
    $mediaModal.droppedImage = file
    $('#mediaImageFile').val(null)
    $mediaModal.loadThumbnail();
  } else {
    swal("Erro", "Apenas imagens são permitidas", "error")
  }

  $(this).css({
    opacity: 1
  })
})

// Enviar
$(".main-form").submit(function (e) {
  e.preventDefault()
})

// Requisitos Técnicos
$('.card-requisito').click(function () {
  $forms.formRequisitos.toggleSelected(this)
})

// Ranking
$(".card-candidato[data-id]").click(function () {
  var id = $(this).attr('data-id')
  if(id){
    location.href = "/curriculo/" + id
  }
})

// Teste Gestor
$("#btnAgendarEntrevista").click(function () {
  swal({
    title: "Agendar estrevista",
    text: "Tem certeza que deseja agendar a entrevista com essa usuário?",
    icon: "info",
    buttons: true,
    dangerMode: true,
  }).then(function (agendar) {
    if (agendar) {

      var idTeste = $("#idTeste").val(),
        url = '/testes_psicologicos/' + idTeste + '/'

      $forms.prepareRequest(url, {
        marcar_entrevista: true
      }, 'PATCH')
        .then(function () {
          swal("Sucesso", "A entrevista foi agendada", "success")
            .then(() => {
              location.reload()
            })
        })
    }
  })
})

// COMPETÊNCIAS

$("#btnSalvarCompetencias, #btnFinalizarCompetencias").click(function () {
  var idAvaliacao = $("#idAvaliacao").val()

  // Lista de competências
  var competencias = []

  // Itera as competências
  $('.card-competencia').each(function () {
    var idItemCompetencia = $(this).attr('data-id-item-competencia'),
      idCompetencia = $(this).attr('data-id-competencia'),
      respostaCompetencia = $(this).find('.status-regua').text(),
      notaCompetencia = $(this).find('.slider').val()

    respostaCompetencia = respostaCompetencia.substring(0, 2).toUpperCase()

    competencias.push({
      id: idItemCompetencia,
      resposta: respostaCompetencia,
      nota: Number(notaCompetencia),
      avaliacao_desempenho: idAvaliacao,
      competencia: idCompetencia
    })
  })

  // Cria as Promises

  var promises = []

  competencias.forEach(function (competencia) {
    promises.push($forms.prepareRequest('/itens_competencias/' + competencia.id + '/', competencia, 'PUT'))
  })

  $forms.setLoading(true)

  var finalizada = $(this).attr('id') == "btnFinalizarCompetencias" ? true : false

  // Envia as requisições
  Promise.all(promises)
    .then(function () {
      swal("Sucesso", "As competencias foram salvas", 'success')
        .then(function () {
          if (finalizada) {
            location.href = "/avaliacoes/"
          }
        })

      // Altera para avaliação respondida
      var dataAtual = new Date(Date.now()).toISOString().split('T')[0]
      $forms.prepareRequest('/avaliacoes_desempenhos/' + idAvaliacao + "/", {
        data: dataAtual,
        pessoa: $("#idPessoaAvaliacao").val(),
        respondida: finalizada,
        comentario: $("#comentario").val()
      }, "PUT")

    })
    .catch(function () {
      swal("Erro", "Ocorreu um erro, fale com o Administrador", 'error')
    })
    .finally(function () {
      $forms.setLoading(false, $(this).text())
    })

})


// Avaliação Metas
$("#btnAddMeta").click(function () {
  $forms.formAvaliacaoMetas.new()
})

$("#btnSalvarAvaliacaoMetas").click(function () {
  if (validateFields()) {
    $forms.formAvaliacaoMetas.submit()
  }
})

// Potencial

$(".btn-salvar-potencial").click(function () {
  var cardCandidato = $(this).parents('.card-candidato')
  idAvaliacao = $(this).parents('.card-candidato').attr('data-id-avaliacao'),
    selectPotencial = $(this).parents('.card-candidato').find('.resposta-potencial'),
    respostaPotencial = selectPotencial.val()

  selectPotencial.removeClass('is-invalid')

  var isEditing = cardCandidato.hasClass('card-yellow') ? false : true

  if (!respostaPotencial) {
    selectPotencial.addClass('is-invalid').focus()
  } else {

    $forms.prepareRequest('/avaliacoes_desempenhos/' + idAvaliacao + '/', {
      resposta_potencial: respostaPotencial
    }, 'PATCH')
      .then(function () {
        $(cardCandidato).removeClass('card-yellow')
        swal("Avaliação de Potencial", "As alterações foram salvas", "success")
      })
  }

})

// Resetar Senha
$(".btn-salvar-senha").click(function () {
  event.preventDefault()
  if (validateFields()) {

    var novaSenha = $("#novaSenha").val(),
      confirmacaoSenha = $("#confirmacaoSenha").val(),
      senhaAtual = $("#senhaAtual").val();

    if (novaSenha.length < 5) {
      swal("Erro", "Digite uma senha com, no mínino, 5 caracteres", "error")
    } else if (novaSenha != confirmacaoSenha) {
      swal("Erro", "As senhas não conferem", "error")
    } else {
      $.ajax({
        type: 'PUT',
        url: '/core/change_password/',
        data: {
          old_password: senhaAtual,
          new_password: novaSenha
        }
      })
        .fail(function () {
          swal("Erro", "A senha atual não está correta", "error")
        })
        .done(function () {
          swal("Sucesso", "A senha foi alterada", "success")
            .then(function () { location.reload() })
        })
    }
  }
})

// Login

$("#id_login").mask('000.000.000-00')

if(localStorage.getItem('EICON_PRIVACIDADE')){
  $("#btnLogin").removeClass('disabled')
  $("input#privacidade").prop('checked', true)
}

$("#btnLogin").click(function(){
  localStorage.setItem("EICON_PRIVACIDADE", true)  
})

$("input#privacidade").change(function(){
  if($(this).prop('checked')){
    $("#btnLogin").removeClass('disabled')
  } else {
    $("#btnLogin").addClass('disabled')
  }
})

// Comitê
$(".btn-avaliar-comite").click(function(){
  var card = $(this).parents('.card-candidato'),
    idAvaliacao = $(card).attr('data-id-avaliacao'),
    resultadoComite = $(card).find('select').val();

  $forms.prepareRequest('/avaliacoes_desempenhos/' + idAvaliacao + "/", {
    resultado_comite: resultadoComite
  }, "PATCH")
  .then(function(){
    swal("Sucesso", "O resultado do comitê foi alterado", "success")
  })
  .catch(function(err){
    $forms.showErrorAlert(err)
  })

  event.stopPropagation()

})