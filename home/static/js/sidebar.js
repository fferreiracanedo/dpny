var isMobile = $(window).width() < 820 ? true : false

var $sidebar = {

  openned: isMobile ? false : true,

  init() {

    var isStaff = $("#sideMenu #isStaff").val() == "True" ? true : false
    $("#sideMenu #isStaff").remove()

    if(isStaff){
      var section = localStorage.getItem("menu_section");
      if(section == "candidato"){
        // Se for candidato
        $("[data-sideview='candidato']").removeClass('d-none')
      } else {
        // Se for gestor
        $("[data-sideview='gestor']").removeClass('d-none')
        section = "gestor"
      }
    } else {
      $("[data-sideview='candidato']").removeClass('d-none')
      section = "candidato"
    }

    $("#sideMenu div[data-sideview], .sideload-container").not("[data-sideview='" + section + "']").remove()

    // Verifica o menu que vai estar ativo
    $("#sideMenu").removeClass('active')
    var path = $(location).attr('pathname')
    path = path.replace('/', '')

    
    path = path.split('/')
    
    var index = path[1] == "" ? 0 : 1
    path = path[index]

    var links = $(".sidebar-container a").not('[data-toggle="collapse"] a').removeClass('active')

    if(path){
      $(links).each(function(index){
        if(path){
          if($(this).attr('href').split('/').indexOf(path) != -1){
            $(this).parent().addClass('active')
          }
        }
      })
    } else {
      $(links).first().parent().addClass('active')
    }

  },

  // Abre e fecha a Sidebar
  toggle() {
    var sidebarElement = $(".sidebar-container"),
      overlayElement = $(".sidebar-overlay")
    if (this.openned) {
      // Fecha a sidebar
      sidebarElement.css({
        width: 0
      })

      overlayElement.css('display', 'none')

    } else {
      // Abre a sidebar
      sidebarElement.css({
        width: isMobile ? '80%' : '400px'
      })

      overlayElement.css('display', 'block')

    }
    this.openned = !this.openned
  },

  // Altera o menu ativo
  setActiveMenuItem(menuItem) {

    var formLink = $(menuItem).find('a').attr('href')
    location.href = formLink

    if (isMobile && this.openned) {
      this.toggle();
    }
  },

  changeUserPhoto(photoFile){
    $forms.convertToBase64(photoFile).then(function (r){
      var photo = r.foto

      $forms.prepareRequest('/pessoas/' + idPessoa + '/', {
        foto: photo
      }, 'PATCH')

      $('#userPhoto').css({
        backgroundImage: 'url(' + photo + ')'
      })
    })
  },

  setSection(section){
    localStorage.setItem('menu_section', section)
    if(section == "candidato"){
      location.href = "/"
    } else {
      location.reload()
    }
  }

}

$sidebar.init()