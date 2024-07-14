$("#id_endereco-0-estado").change(function() {
    $.ajax({
      type: 'POST',
      url: '/on_change_estado/',
      data: {
          'estado': $("#id_endereco-0-estado").val()
      },
      success: function(data) {
          $("#id_endereco-0-cidade").children('option:not(:first)').remove();

          var cidades = JSON.parse(data)

          for (i=0; i<cidades.length; i++){
              $("#id_endereco-0-cidade").append('<option value="'+cidades[i]["pk"]+'">'+cidades[i]["fields"]["nome"]+'</option>');
          }
      }
    });
});

$("#id_endereco_set-0-estado").change(function() {
    $.ajax({
      type: 'POST',
      url: '/on_change_estado/',
      data: {
          'estado': $("#id_endereco_set-0-estado").val()
      },
      success: function(data) {
          $("#id_endereco_set-0-cidade").children('option:not(:first)').remove();

          var cidades = JSON.parse(data)

          for (i=0; i<cidades.length; i++){
              $("#id_endereco_set-0-cidade").append('<option value="'+cidades[i]["pk"]+'">'+cidades[i]["fields"]["nome"]+'</option>');
          }
      }
    });
});