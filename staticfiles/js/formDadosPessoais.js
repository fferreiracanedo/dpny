

var allEstados;

$.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados/", function (estados) {

  // Estados na ordem alfabética
  estados.sort(function (a, b) {
    var textA = a.nome.toUpperCase();
    var textB = b.nome.toUpperCase();
    return (textA < textB) ? -1 : (textA > textB) ? 1 : 0;
  });

  // Adiciona no Select
  estados.forEach(function (estado) {
    $("#estado").append("<option value='" + estado.sigla + "'>" + estado.nome + "</option>")
    $("#ufCTPS").append("<option value='" + estado.sigla + "'>" + estado.sigla + "</option>")
  })

  allEstados = estados;

  $("#estado").removeAttr('disabled')
})

var lastCidade = null;

$("#estado").change(function () {

  // Acha o estado selecionado
  var idEstado = allEstados.find(function (estado) {
    return estado.sigla == $("#estado").val()
  }).id

  $("#cidade").attr('disabled', 'disabled')

  // Pega as cidades do estado selecionado
  $.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados/" + idEstado + "/municipios", function (cidades) {
    // Adiciona no Select
    $("#cidade").empty()
    cidades.forEach(function (cidade) {
      $("#cidade").append("<option value='" + cidade.nome + "'>" + cidade.nome + "</option>")
    })
    $("#cidade").removeAttr('disabled')

    if (lastCidade) {
      $("#cidade").val(lastCidade)
      lastCidade = null
    }

  })

})

$("#cep").mask("00000-000", {
  onComplete(val) {
    searchCEP(val)
  }
})

function searchCEP(val) {
  val = val.replace('-', '')
  $("#cep").addClass('disabled')
  $.get('https://viacep.com.br/ws/' + val + '/json/', function (res) {
    if (res.erro == true) {
      alert("O CEP inserido é invalido")
      $("#cep").addClass('is-invalid')
    } else {
      $("#complemento").val(res.complemento)
      $("#bairro").val(res.bairro)
      $("#endereco").val(res.logradouro)
      $("#estado").val(res.uf)

      lastCidade = res.localidade
      $("#estado").change()

    }

    $('#cep').removeClass('disabled')

  })
}

$("#cep").focusout(function () {
  var cep = $(this).val().replace('-', '');

  if (cep.length < 9) {
    var cep = ("00000000" + cep).slice(cep.length)

    cep = [cep.slice(0, 5), '-', cep.slice(5)].join('');

    $(this).val(cep)

    searchCEP(cep)

  }
})

// Filhos

addDadosPessoaisActions()

function addDadosPessoaisActions() {
  // Clicar pra adicionar mídia
  $(".btn-filho-cpf-media, .btn-editar-cpf-filho").click(function () {
    $(this).parents('.form-group').find('input[type=file]').trigger('click')
  })

  // Upload dos documentos dos filhos
  $(".field-filho input[type=file]").change(function () {

    var image = this.files[0],
      docElement = $(this).parents('.doc')
    alertElement = $(docElement).find('.alert')

    // Cria um link para a imagem
    fileReader = new FileReader();
    fileReader.onloadend = function () {
      docElement.attr('data-img-src', fileReader.result)
      alertElement.removeClass('d-none')
      $(docElement).find('.btn-filho-cpf-media').addClass('d-none')
    }

    if (image) {
      fileReader.readAsDataURL(image)
    }
  })

  // Modal documento
  $(".ver-doc").click(function () {
    // Pega a imagem e a ID do documento
    var src = $(this).parents('.doc').attr('data-img-src'),
      docId = $(this).parents('.doc').attr('data-doc');

    // Abre o Modal
    $("#fotoDocumento").attr('src', src)
    if (docId == "CPF Dependente") {
      $("#btnExcluirDocumento").addClass('d-none')
    } else {
      $("#btnExcluirDocumento").removeClass('d-none')
    }

    $("#modalImagem").attr('data-doc-id', docId).modal()
  })

}

function toggleRemoverFilho() {
  // Decide se o botão de remover filho estará visível
  if ($('.field-filho').length > 1) {
    $('#btnRemoverFilho').removeClass('d-none')
  } else {
    $('#btnRemoverFilho').addClass('d-none')
  }
}

$("#btnAdicionarFilho").click(function () {
  // Adicionar um novo filho
  var fields = $(".field-filho").first().clone()
  fields.removeAttr('data-filho-id')
  fields.find('input').val("")
  fields.find('.btn-filho-cpf-media').removeClass('d-none')
  fields.find('.doc').attr('data-img-src', '')
  fields.find('.alert').addClass('d-none')
  fields.insertAfter($(".field-filho").last())
  $('.cpf-filho').mask('000.000.000-00')
  toggleRemoverFilho()
  addDadosPessoaisActions()
})

$("#btnRemoverFilho").click(function () {
  // Remove um filho
  var lastFilho = $('.field-filho').last()

  var id = lastFilho.attr('data-filho-id')
  lastFilho.remove()

  $forms.prepareRequest('/filhos/' + id + '/', null, 'DELETE')

  toggleRemoverFilho()
})

$("#estadoCivil").change(function () {
  if ($(this).find("option:selected").text().toLowerCase().indexOf("divorciado") != -1) {
    $(".doc-divorcio").removeClass('d-none')
  } else {
    $(".doc-divorcio").addClass('d-none')
  }
})

// Upload dos documentos
$("#docFiles input[type=file], .doc-divorcio-anexo input[type=file]").change(function () {
  var image = this.files[0],
    alertElement = $(this).prev('.alert')
  docElement = $(this).parents('.doc')

  // Cria um link para a imagem
  fileReader = new FileReader();
  fileReader.onloadend = function () {
    docElement.attr('data-img-src', fileReader.result)
    alertElement.find('.doc-link').attr('href', fileReader.result)
    alertElement.removeClass('d-none')
    alertElement.find('.doc-date').text(new Date(Date.now()).toLocaleDateString())
  }

  if (image) {
    fileReader.readAsDataURL(image)
  }
})

$('.doc-link').click(function(){
  var href = $(this).attr('href')

  if(href.indexOf('base64,') != -1){
    const win = window.open("","_blank");
    let html = '';
    
    html += '<html>';
    html += '<body style="margin:0!important">';
    html += '<embed width="100%" height="100%" src="'+ href +'" type="application/pdf" />';
    html += '</body>';
    html += '</html>';
    
    setTimeout(() => {
      win.document.write(html);
    }, 0);  }

})

$("#btnExcluirDocumento").click(function () {

  // Confirmação para excluir
  swal({
    title: "Apagar documento",
    text: "Tem certeza que deseja apagar esse documento?",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then(function (canDelete) {
    if (canDelete) {
      // Pega a ID do documento
      var docId = $("#modalImagem").attr('data-doc-id'),
        docElement = $(".doc[data-doc='" + docId + "']");

      // Requisição para excluir o documento
      $forms.prepareRequest('/pessoas/' + idPessoa + '/' + docId + '/', null, 'DELETE')

      // Apaga o documento
      docElement.find('input[type=file]').val("")
      docElement
        .removeAttr('data-img-src')
        .find('.alert').addClass('d-none')
      $("#modalImagem").modal('hide')
    }
  })

})

$("#videoFile").change(function () {
  var video = $(this)[0].files[0]
  if (video) {

    if (video.type.indexOf('video') != -1) {
      $forms.convertToBase64(video).then(function (r) {
        $("#videoContainer").removeClass('d-none')
        $("#videoContainer video").remove()
        $("#btnCarregarVideo").addClass('disabled')

        var videoElement = ""
        videoElement += "<video  autoplay controls id='uploadedVideo'>"
        videoElement += "<source src='" + r.foto + "' type='" + video.type + "'>"
        videoElement += "</video>"

        $("#videoContainer").prepend(videoElement)

      })
    } else {
      swal("Erro", "Faça upload de um video", "error")
    }

  }
})

$("#btnRemoverVideo").click(function () {
  swal({
    title: "Remover Video",
    text: "Tem certeza que deseja remover esse video?",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then(function (remover) {
    if (remover) {
      $("#videoContainer").addClass('d-none')
      $("#btnCarregarVideo").removeClass('disabled')
      $("#videoFile").val('')
      $("#videoContainer video").remove()
      $forms.prepareRequest('/pessoas/' + idPessoa + '/', {
        video: null
      }, "PATCH")

    }
  })
})

$("#curriculoFile").change(function () {
  var curriculo = $(this)[0].files[0];
  if (curriculo) {
    $forms.convertToBase64(curriculo).then(function (r) {

      var mime = curriculo.name.split('.');
      mime = mime.slice(-1)[0]

      var file = r.foto;
      $('.curriculo .alert').removeClass('d-none')
      $("#btnBaixarCurriculo")
        .attr({
          href: file,
          download: 'curriculo.' + mime
        })

      $('.curriculo .media-title').text(curriculo.name)
    })
  }
})

// Pega a ID da Pessoa
var idPessoa = $("#idPessoa").val()
$("#idPessoa").remove()

// Vê se é funcionário
var isFuncionario = $("#cargoPessoa").val() ? true : false
$("#cargoPessoa").remove()

$(".btn-salvar-dados-pessoais").click(function () {

  var validate = validateDadosPessoais()

  // Executa somoente se todos os campos estiverem válidos
  if (validate.isValid) {
    // Pega os dados das campos
    var dadosPessoais = $forms.serializeFieldContainer($(".form-content"));

    // Iterar os Documentos
    $("#docFiles, .doc-divorcio").find(".doc").each(function () {

      try {
        // Pega os dados dos documentos
        var nomeDoc = $(this).attr('data-doc'),
          docFile = $(this).attr('data-img-src')
        
        var mimeFile = "";

        if(docFile.indexOf('base64,') != -1){
          mimeFile = docFile.split(';')[0].split('/')[1]
        }

        // Se não for base64 deixa como nulo
        if (docFile.indexOf('base64,') == -1) {
          docFile = null
        }

        if(mimeFile){
          dadosPessoais[nomeDoc] = mimeFile + "-" + docFile
        } else {
          dadosPessoais[nomeDoc] = docFile
        }

      } catch (error) { }
    })

    // Se for funcioário
    if (validate.type == "funcionario") {

      // Cria array de filhos
      var filhos = []

      // Iterar os filhos
      $(".field-filho").each(function () {
        var nome = $(this).find('.nome-filho').val(),
          dataNascimento = $(this).find('.nascimento-filho').val()
        cpf = $(this).find('.cpf-filho').val()
        fotoCpf = $(this).find('.doc').attr('data-img-src')

        // Não adicionar na array se um dos campos estiver vazio
        // if (!nome || !dataNascimento) return

        var filho = {
          id: $(this).attr('data-filho-id'),
          nome: nome,
          data_nascimento: dataNascimento,
          cpf: cpf
        }

        if (fotoCpf) {
          if (fotoCpf.indexOf('base64,') != -1) {
            filho.cpf_anexo = fotoCpf
          }
        }

        filhos.push(filho)
      })

    } else {
        // Pega o video
        if (!$('#videoContainer').hasClass('d-none')) {
          var video = $("#uploadedVideo source").attr('src')

          if (video.indexOf('base64,') != -1) {
            video = "mp4-" + video;
            dadosPessoais.video = video;
          }

        }

        // Pega o currículo
        if ($("#btnBaixarCurriculo")[0].hasAttribute('download')) {
          var btnCurriculo = $("#btnBaixarCurriculo"),
            curriculo = btnCurriculo.attr('href'),
            mime = btnCurriculo.attr('download').split('.')[1];

          if (curriculo.indexOf('base64,') != -1) {
            curriculo = mime + '-' + curriculo;
            dadosPessoais.curriculo = curriculo
          }

        }
    }

    $forms.setLoading(true)

    // Faz a requição para salvar os filhos
    function saveFilhos() {
      if (filhos) {
        // Itera os filhos
        filhos.forEach(function (filho) {
          if (!filho.id) {
            // Adiciona o filho
            $forms.prepareRequest('/filhos/', filho, 'POST')
              .then(function (res) {
                // Procura o campo do filho correspondente a adiciona a ID
                $(".field-filho").each(function () {
                  if (!$(this)[0].hasAttribute('data-filho-id')) {
                    if ($(this).find('.nome-filho').val() == res.nome &&
                      $(this).find('.nascimento-filho').val() == res.data_nascimento) {
                      $(this).attr('data-filho-id', res.id)
                    }
                  }
                })
              })
          } else {
            // Edita o filho
            $forms.prepareRequest('/filhos/' + filho.id + '/', filho, 'PUT')
          }
        })
      }
      swal("Sucesso", "Os dados foram salvos", "success")
    }

    if (!dadosPessoais.pretensao_salarial) {
      dadosPessoais.pretensao_salarial = 0
    }

    // Faz a requisição para editar a pessoa
    if (idPessoa) {
      $forms.prepareRequest('/pessoas/' + idPessoa + '/', dadosPessoais, "PUT")
        .then(function () {
          saveFilhos()
        })
        .catch(function (err) {
          $forms.showErrorAlert(err)
        })
        .finally(function () {
          $forms.setLoading(false)
        })
    } else {
      $forms.prepareRequest('/pessoas/', dadosPessoais, "POST")
        .then(function () {
          swal("Sucesso", "Os dados foram salvos", "success")
            .then(function () {
              location.reload()
            })
        })
        .catch(function (err) {
          $forms.showErrorAlert(err)
        })
        .finally(function () {
          $forms.setLoading(false)
        })
    }
  }
})


function validateDadosPessoais() {

  var isValid = true;

  // Se for candidato não valida
  if ($('.fields-funcionario').length == 0) {

    // Validação caso o usuário não esteja criado ainda
    if (!isFuncionario) {

      if (isValid) {
        // Valida os outros campos
        if (!$("input[name=nome]").val()) {
          swal("Erro", "Preencha o Nome", "error")
            .then(function () {
              $("input[name=nome]").focus()
            })
          isValid = false
        }
      }

      if (isValid) {
        if ($("input[name=cpf]").val().length < 14) {
          swal("Erro", "Preencha o CPF corretamente", "error")
            .then(function () {
              $("input[name=cpf]").focus()
            })
          isValid = false
        }
      }

      if (isValid) {
        if (!$("input[name=data_nascimento]").val()) {
          swal("Erro", "Preencha a Data de Nascimento", "error")
            .then(function () {
              $("input[name=data_nascimento]").focus()
            })
          isValid = false
        }
      }

      if (isValid) {
        if (!isEmailValid($('input[name=email]').val())) {
          swal("Erro", "Preencha o email corretamente", "error")
            .then(function () {
              $("input[name=email]").focus()
            })
          isValid = false
        }
      }

      if (isValid) {
        if (!$("input[name=telefone]").val()) {
          swal("Erro", "Preencha o Telefone", "error")
            .then(function () {
              $("input[name=telefone]").focus()
            })
          isValid = false
        }
      }

    }

    return {
      isValid: isValid,
      type: "candidato"
    }
  }


  // Se for funcionário, faz a validação
  var container = $("#formDadosPessoais")
  var fields = container.find('input, select').not("[type=file], .field-filho input, .no-validate")

  if (!$("#nome").val() || !$("#cpf").val()) {
    swal("Erro", "Preencha pelo menos os campo Nome e CPF", "error")
    isValid = false
  }

  // Retorna o resultado
  return {
    isValid: isValid,
    type: "funcionario"
  }


  /*  
  
    VALIDAÇÃO ANTIGA (TODOS OS CAMPOS)
  
  */

  for (fieldEl of fields) {
    // Pega os dados de cada campo
    var field = {
      name: $(fieldEl).parent().find('label').text().replace('*', ''),
      value: $(fieldEl).val() || "",
      mask: $(fieldEl).attr('data-mask'),
      minLength: $(fieldEl).attr('minlength') || 1,
    }

    // Valida o campo Email
    if ($(fieldEl).attr('type') == 'email') {
      if (!isEmailValid(field.value)) {
        swal("Erro", "Preencha o email corretamente", "error")
          .then(function () {
            $(fieldEl).focus()
          })
        return false
      }
    }

    // Valida os outros campos
    if ((field.mask && field.value.length < field.mask.length) || (field.value.length < field.minLength)) {
      swal("Erro", 'Preencha o campo "' + field.name + '"', "error")
        .then(function () {
          $(fieldEl).focus()
        })
      return false
    }
  }

  isValid = true;

  // Valida os filhos
  $(".field-filho").each(function (i) {
    var fieldNome = $(this).find('.nome-filho'),
      fieldNascimento = $(this).find('.nascimento-filho')
    fieldCPF = $(this).find('.cpf-filho')

    var numeroFilho = (Number(i) + 1);

    if (!fieldNome.val() && !fieldNascimento.val() && !fieldCPF.val()) {
      if ($('.field-filho').length > 1) {
        $(this).remove()
      }
    } else if (fieldNome.val() && !fieldNascimento.val()) {
      swal("Erro", 'Insira a data de nascimento do ' + numeroFilho + 'º Filho', "error")
        .then(function () {
          $(fieldNascimento).focus()
        })
      isValid = false
      return false
    } else if (!fieldNome.val() && fieldNascimento.val()) {
      swal("Erro", 'Insira o nome do ' + numeroFilho + 'º Filho', "error")
        .then(function () {
          $(fieldNome).focus()
        })
      isValid = false
      return false
    } else if (fieldCPF.val().length != 14) {
      swal("Erro", 'Insira o CPF do ' + numeroFilho + 'º Filho corretamente', "error")
        .then(function () {
          $(fieldCPF).focus()
        })
      isValid = false
      return false
    }
  })

  // Iterar os Documentos
  $("#docFiles").find(".doc").each(function () {
    if (isValid) {
      var image = $(this).attr("data-img-src"),
        nomeDoc = $(this).find('.media-title').text()

      if (!image) {
        swal("Documento", "Carregue o " + nomeDoc, "error")
        isValid = false
      }

    }
  })

  // Retorna o resultado
  return {
    isValid: isValid,
    type: "funcionario"
  }

}


function isEmailValid(text) {
  if (text.indexOf("@") == -1
    || text.indexOf(".") == -1
    || text.length < 5
  ) {
    return false
  } else {
    return true
  }
}

// Remove as marcações de validação
if(isFuncionario){
  $("#telefoneResidencial, #email, #dataNascimento").parent().find('label').each(function(){
    $(this).text($(this).text().replace('*', ''))
  })
}