
var nome_entrada = document.getElementById('nome');
var email_entrada = document.getElementById('email');
var senha_entrada = document.getElementById('senha');
var confirmacao = document.getElementById('confirmasenha');


function senha_errada() {

    if (senha_entrada.value.trim() == '' || confirmacao.value.trim() == '') {
        senha_entrada.style.backgroundColor = "#dcdcdc80";
        confirmacao.style.backgroundColor = "#dcdcdc80";
    }


}


function cadastrando_usuario() {


    if (nome_entrada.value.trim() != '' && email_entrada.value.trim() != '' && senha_entrada.value.trim() != '' && confirmacao.value.trim() != '') {

        if (senha_entrada.value.trim() == confirmacao.value.trim()) {

            alert('Dados salvos com sucesso!!!');

        } else {
            senha_entrada.style.backgroundColor = "#ffb0a0";
            confirmacao.style.backgroundColor = "#ffb0a0";
            alert('Você inseriu senhas diferentes!!!');
        }

        dados.usuarios.nome = nome_entrada;
        alert('dados salvos');
    } else {
        alert('PREENCHA TODOS OS CAMPOS');
    }




}
