//função que não deixa escrever letras no campo de números
function onlynumber(evt) {
    var theEvent = evt || window.event;
    var key = theEvent.keyCode || theEvent.which;
    key = String.fromCharCode( key );
    //var regex = /^[0-9.,]+$/;
    var regex = /^[0-9.]+$/;
    if( !regex.test(key) ) {
       theEvent.returnValue = false;
       if(theEvent.preventDefault) theEvent.preventDefault();
    }
 }

 //impedindo o usuário de enviar com campos em branco
function validarFormulario(){
    var sobrenome = document.forms["formulario"]["sobrenome"].value;
    if (sobrenome == "") {
        alert("ATENÇÃO!! Favor informar o seu nome!");
        return false;
    }
    var nome = document.forms["formulario"]["nome"].value;
    if (email == "") {
        alert("ATENÇÃO!! Favor informar o seu email!");
        return false;     
    }
    var telefone = document.forms["formulario"]["telefone"].value;
    if (telefone == "") {
        alert("ATENÇÃO!! Favor informar o seu telefone!");
        return false;     
    }
}

//confirmar inscrição

function enviar(){
    window.confirm("Confirmar envio os dados?")
}

//capturando nome, sobrenome e idade da pessoa ao acessar o site
var sobrenome = prompt('Qual seu sobrenome?');
var nomePessoa = prompt('Qual é o seu nome?');
var idade = parseInt(prompt('Qual a sua idade?'));
alert('Olá '  + nomePessoa +', espero que estejas bem!');    
document.write(`Seu nome completo é ${nomePessoa} ${sobrenome} e você possui ${idade} anos de idade.`);





/*var sobrenome1 = document.getElementById("txtsobrenome").value;
ar nome1 = document.getElementById("txtnome").value;
var telefone1 = document.getElementById("txttelefone").value;
console.log(`${sobrenome1}`)
*/