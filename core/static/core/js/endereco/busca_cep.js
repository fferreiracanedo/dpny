$("#id_endereco-0-cep").change(function() {
    $.ajax({
      type: 'POST',
      url: '/buscar_cep/',
      data: {
          'cep': $("#id_endereco-0-cep").val()
      },
      success: function(data) {
          $("#id_endereco-0-logradouro").val(data.logradouro);
          $("#id_endereco-0-bairro").val(data.bairro);
          $("#id_endereco-0-pais").val(data.pais);
          $("#id_endereco-0-estado").val(data.estado);
          $("#id_endereco-0-cidade").val(data.cidade);
      }
    });
});

$("#id_endereco_set-0-cep").change(function() {
    $.ajax({
      type: 'POST',
      url: '/buscar_cep/',
      data: {
          'cep': $("#id_endereco_set-0-cep").val()
      },
      success: function(data) {
          $("#id_endereco_set-0-logradouro").val(data.logradouro);
          $("#id_endereco_set-0-bairro").val(data.bairro);
          $("#id_endereco_set-0-pais").val(data.pais);
          $("#id_endereco_set-0-estado").val(data.estado);
          $("#id_endereco_set-0-cidade").val(data.cidade);
      }
    });
});