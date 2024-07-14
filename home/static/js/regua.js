$(window).ready(function(){
  $('.card-competencia .slider').each(function(){
    updateSlider($(this))
  })
})

$('.slider').on('input', function(){
  updateSlider($(this))
})

function updateSlider(slider){
  var value = Number($(slider).val())

  var indicator = $(slider).parent().find('.slider-indicator')

  indicator.css({
    left: value + "%"
  })

  indicator.text(value)

  var status = $(slider).parents('.card-competencia').find('.status-regua')

  if(value >= 0 && value <= 25){
    status.text('Raramente').css('color', '#e63211')
  } else if (value >= 26 && value <= 50){
    status.text('Ocasionalmente').css('color', '#fca70d')
  } else if (value >= 51 && value <= 75){
    status.text('Constantemente').css('color', '#45beae')
  } else if (value >= 76){
    status.text('Exarcebadamente').css('color', '#45beae')
  }
}