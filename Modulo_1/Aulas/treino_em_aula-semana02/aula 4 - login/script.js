function validar(){
    var usuario = document.getElementById("usuario").value;
    var senha = document.getElementById("senha").value;

    if (usuario == "aluno" && senha == "1234"){
        alert("Login foi realizado com sucesso!");
    }
    else{
        alert("O seu login está errado.");
    }
}