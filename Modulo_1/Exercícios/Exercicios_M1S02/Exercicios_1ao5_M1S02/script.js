//validar formulário em branco
function validarFormulario(){
    var nomePessoa = document.forms["inscreva"]["nome"].value;
    if (nomePessoa == "") {
        alert("ATENÇÃO!! Favor informar o seu nome!");
        return false;     
    }
    var email = document.forms["inscreva"]["email"].value;
    if (email == "") {
        alert("ATENÇÃO!! Favor informar o seu email!");
        return false;     
    }
    var telefone = document.forms["inscreva"]["telefone"].value;
    if (telefone == "") {
        alert("ATENÇÃO!! Favor informar o seu telefone!");
        return false;     
    }
    var idade = document.forms["inscreva"]["idade"].value;
    if (idade == ""){
        alert("ATENÇÃO!! Insira uma data de nascimento.")
        return false;
    }
    else{
        alert("Olá, " + nomePessoa + "! Sua inscrição foi concluída! Seu login e senha foram enviados para seu email. Obrigado e boa viagem!");
        return true;
    }
}
//confirmar inscrição
function enviar(){
    alert("Confirmar enviar os dados?")
}