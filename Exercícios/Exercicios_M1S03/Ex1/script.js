//capturando as variáveis via prompt
var nome = prompt("Qual é o seu nome?");
var idade = parseInt(prompt("Qual a sua idade?"));
var exercicio = confirm("Você deseja fazer exercícios?");

//verificando o confirma/cancela - retornando o resultado na tela
/*
if (exercicio == true){
    document.write(`Seu nome é ${nome}, sua idade é ${idade} anos e você deseja fazer exercícios!`);
} else {
    document.write(`Seu nome é ${nome}, sua idade é ${idade} anos e você não deseja fazer exercícios.`);
} 
*/ 

//verificando o confirma/cancela - retornando o resultado via alert
if (exercicio == true){
    alert(`Seu nome é ${nome}, sua idade é ${idade} anos e você deseja fazer exercícios!`);
} else {
    alert(`Seu nome é ${nome}, sua idade é ${idade} anos e você não deseja fazer exercícios.`);
}