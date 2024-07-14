function validarTamanho(inputField) {
    var file;
    var tamanhoMaximo = 2000000;

    if (!window.FileReader) {
        return true;
    }

    if (!inputField) {
        return true;
    }
    else if (!inputField.files) {
        return true;
    }
    else if (!inputField.files[0]) {
        return true;
    }
    else {
        file = inputField.files[0];
        console.log(file.size);
        console.log(tamanhoMaximo);

        if (parseFloat(file.size) > parseFloat(tamanhoMaximo)){
            console.log('Arquivo excede o tamanho máximo permitido!');
            return false;
        }else{
            console.log('Arquivo aprovado para envio!');
            return true;
        }

    }
}

document.getElementById("id_video").onchange = function(){
    if (!validarTamanho(this)){
        alert("Arquivo de vídeo muito grande, por favor, selecionar um arquivo menor! Tamanho máximo (2MB)");
        document.getElementById("id_video").value = "";
    }
}

document.getElementById("id_foto").onchange = function(){
    if (!validarTamanho(this)){
        alert("Arquivo de foto muito grande, por favor, selecionar um arquivo menor! Tamanho máximo (2MB)");
        document.getElementById("id_foto").value = "";
    }
}

document.getElementById("id_curriculo").onchange = function(){
    if (!validarTamanho(this)){
        alert("Arquivo de curriculo muito grande, por favor, selecionar um arquivo menor! Tamanho máximo (2MB)");
        document.getElementById("id_curriculo").value = "";
    }
}