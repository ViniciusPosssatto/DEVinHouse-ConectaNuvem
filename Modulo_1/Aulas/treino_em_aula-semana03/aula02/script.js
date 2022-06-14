console.log('funciona?');

var listaDeLinguagens = ['C', 'JavaScript', 'python'];

//empurra um item dentro da lista
listaDeLinguagens.push = ('php');

//retira o último elemento da lista (sem contar o que foi colocado via push)
listaDeLinguagens.pop()

//utiliza uma função
listaDeLinguagens.forEach(function (elemento, índice, array) { //essa função possui 3 parâmetros function ( 1º, 2º, 3º) 1º é o item da lista(elemento)/2º é o índice de onde está o elemento/3º é o próprio array(caso queira usar o próprio array na função)
    console.log('A'); //vai imprimir 3vz A (1 vez para cada item do array listadeLinguagens)
});

console.log(listaDeLinguagens);

// utilizando for
var langList = ['C', 'JavaScript', 'python'];
for (var i = 0; i < langList.length; i++);
//código a executar
console.log(langList)


var listaDeCarros = ['uno', 'fusca', 'escort', 'gol'];
for (var carro of listaDeCarros) {  //funciona pro for in tbm
 if (carro === 'uno') continue;  //carro é igual a uno, porém o continue vai fazer com que o código continue mesmo que já estaria certo
 if (carro === 'escort') break;  //quando executar o break, o código para
 console.log(carro); //nesse caso vai imprimir apenas 'fusca' pois quando foi dado continue no uno ele pulou e quando foi dado break no escort não contou ele.
}

//imprimindo todos os itens da lista usando for
for (var i = 0; i < listaDeCarros; i++) {
    console.log(listaDeCarros[i]);
}

//FUNÇÕES
function nomeDaFuncao (parametros){
    var resultado = parametros + (algumacoisa) //no caso utiliza-se os parametros designados para obter o resultado desejado
    return resultado;
}

function f(x, y){
    var resultado = x**2 + (x + y);
    return resultado;
}

var retorno = f(2, 1); //chama a função, substitui o x e y pelos valores respectivos e executa a var resultado

console.log(retorno); //apresenta o resultado da função

//montando uma lista por push
function preencheVetor(n) {
    var vetor = []
    for (var i = 0; i <= n; i++) {
        vetor.push(i) //vai empurrar elementos de i na lista vetor
    }
    return vetor;
}

console.log(preencheVetor(9)); //vai montar uma lista na variavel vetor de 0 até 9 nesse caso

/*************///////////////////*/************************************* */ */
//EVENTOS

var botao = document.getElementById('botao');  //captura um evento de click do html com id botao
var campo = document.getElementById('entrada'); //captura elementos de um campo de texto no html com id campo

function lidaComClick() {
    console.log('Clicou'); //imprime no console (clicou)
    console.count('clicou'); //imprime no console a contagem de cliques 
}

botao.onclick = lidaComClick;  //evento onclick vai executar a função lidacomclick

botao.addEventListener('Click', lidaComClick); //outra forma de atribuir o valor de clicar('click') chamando a função
//****utilizar esse formato por boas praticas e também porque da pra atribuir mais de um evento no mesmo botao, sendo q no on click só da pra fazer um evento

campo.onkeydown = function () {
    console.log('Apertou uma tecla'); //imprime no console cada vez que alguem clicou em uma letra no campo
}

