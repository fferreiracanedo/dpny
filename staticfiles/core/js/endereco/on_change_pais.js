$("#id_endereco-0-pais").change(function() {
    $.ajax({
      type: 'POST',
      url: '/on_change_pais/',
      data: {
          'pais': $("#id_endereco-0-pais").val()
      },
      success: function(data) {
          $("#id_endereco-0-estado").children('option:not(:first)').remove();

          var estados = JSON.parse(data)

          for (i=0; i<estados.length; i++){
              $("#id_endereco-0-estado").append('<option value="'+estados[i]["pk"]+'">'+estados[i]["fields"]["nome"]+'</option>');
          }
      }
    });
});

$("#id_endereco_set-0-pais").change(function() {
    $.ajax({
      type: 'POST',
      url: '/on_change_pais/',
      data: {
          'pais': $("#id_endereco_set-0-pais").val()
      },
      success: function(data) {
          $("#id_endereco_set-0-estado").children('option:not(:first)').remove();

          var estados = JSON.parse(data)

          for (i=0; i<estados.length; i++){
              $("#id_endereco_set-0-estado").append('<option value="'+estados[i]["pk"]+'">'+estados[i]["fields"]["nome"]+'</option>');
          }
      }
    });
});