console.log('funciona!');


// -----------------------------------exemplos JSON e LocalStorage

// var carro = {
//   ano: 2000,
//   modelo: 'Corolla',
//   marca: 'Toyota'
// };

// var carroJSON = JSON.stringify(carro);

// console.log(carro);
// console.log(carroJSON);

//localStorage.setItem('carro', carroJSON);

//var cJSON = localStorage.getItem('carro');

// exemplod e console.log com multiplas variaveis
// var ano = 1999;
// var mes = 12;
// var dia = 15;

// console.log('LOG_1', {
//   ano,
//   mes,
//   dia
// });



//  __--------------------------------------------ECMAScript

// escopo global
var global = 'estou no escopo global';

// escopo de função
function funcao() {
  var func = 'estou no escopo de função';
}

// escopo de bloco
if (funcao) {
  var bloco = 'estou no escopo de bloco';
  console.log(bloco);  // aqui vai funcionar pq o console está dentro do escopo de função 
}

console.log(bloco); // isso vai resultar em is not defined (porque está tentando apresentar uma variável que estaá dentro de um bloco);


//******************************************************** */
// escopo global
var global = 'estou no escopo global';

// escopo de função
function funcao() {
  var func = 'estou no escopo de função';
  console.log({ global, func });
}

// Exemplos de blocos:
// if, else, for, while, switch
if (funcao) {
  const bloco = 'estou no escopo de bloco';
} 

//console.log({ global, bloco });
//funcao();

// escopo de função
function definirLargura() {
  var largura = 100;
  console.log(largura);
}
definirLargura();
console.log(largura);

// escopo de bloco
// var vaza do escopo de bloco

// var altura = 100;
// if (altura > 90) {
//   var largura = 100;
//   console.log(largura);
// }
// console.log(largura);

// escopo de bloco
// let e const não vazam do escopo de bloco
// const largura = 99;

// if (largura > 90) {
//   const largura = 100;
//   console.log(largura);
// }
// console.log(largura);

// escopo de bloco

// let e const não vazam do escopo de bloco
// let pontos = 50;
// let vencedor = false;
// if (pontos > 40) {
//   console.log('passei pelo if');
//   console.log(vencedor);
//   //let vencedor = true;
// }
// console.log(vencedor);


// exemplo alterar variavel mais externa

// let testeFora = 0;
// function exemplo() {
//   const teste = 5;
//   testeFora = 6;
//   return teste;
// }
// console.log(exemplo(), testeFora);

// exemplo de const modificada internamente

// const nomeVariavel = {};
// nomeVariavel.sfasdf = 'corolla';
// console.log(nomeVariavel);

// exemplo variaveis "içadas"

//console.log(a);
//const a = 6; // gera erro
//var a = 6; // não gera erro

// exemplo de função "içada"

// mostraOi();
// function mostraOi() {
//   console.log('oi')
// }

// exemplos escopo global

//var outraVar = 'ble';
//window.nomeDaVar = 'bla';
//console.log(nomeDaVar);
//console.log(window.outraVar);

var foo = 'batata';

if (1) {
  let foo = 'feijão';
  foo = 'bleleleyu';
  console.log(foo);
  if (1) {
    let foo = 'cebola';
    console.log(foo);
  }
}

console.log(foo);

// a baixo exemplos de classes e objetos

function criaPessoa(nome, idade, rg) {
  const novaPessoa = {}
  novaPessoa.nome = nome
  novaPessoa.idade = idade
  novaPessoa.rg = rg
  return novaPessoa
}
// const pessoa = criaPessoa('Juliana', 26, '7235654453');

class Pessoa {
  constructor(nome, idade, rg) {
    this.nome = nome
    this.idade = idade
    this.rg = rg
  }

  correr() {
    console.log(`${this.nome} está correndo!`);
  }
}

const ju = new Pessoa('Juliana', 26, '7235654453');
const romeu = new Pessoa('Romeu', 29, '7344654453');

console.log(ju, romeu);

console.log(ju.nome)

romeu.correr();

class Template {
  constructor(id, html) {
    this.elem = document.getElementById(id);
    this.html = html;
  }
  modelo(conteudo) {
    return `<span style="color:red">${conteudo}</span>`
  }
  atualiza() {
    this.elem.innerHTML = 
      this.modelo(this.html)
  }
}

const div = new Template('teste', 'oi');
console.log(div)
div.atualiza()