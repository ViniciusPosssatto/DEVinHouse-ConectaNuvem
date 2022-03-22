
console.log('funciona!');

//    índice    0       1        2         3   (conta eles juntos pq foi implementado mais abaixo).
var vetor = ['fusca', 'gol']; //belina   carro

vetor.push('belina');
vetor.push('carro');

console.log(vetor[0]);

// conta o índice a partir do 1 em vez do zero.
console.log(vetor.length);

var texto = ('paralelepipedo0');
//irá fazer a contagem das letras a partir do 1  (nesse caso 15)
console.log(texto.length);
//irá buscar a casa 3 começando de 0 para apresentar no console (nesse caso o 'a')
console.log(texto[3]);

/*
//vai trocar todos os 'd' por @.
var texto2 = ['aadsdsdaassddddrerere'];
var textoNovo = texto2.replaceall('d', '@');
console.log(textoNovo);
*/

//verificar se é PAR ou ímpar (de forma TERNÁRIA)  <--
var a = 4;
a % 2 == 0
    ? console.log(a + ' é par.')
    : console.log(a + ' é ímpar.');


// verificar em 3 etapas de condições (condições aninhadas)
var nome =  'Ada';
var sobrenome = 'Lovelace';
var nomeCompleto = nome + ' ' + sobrenome;
var idade = 36;

if (idade >= 18 && idade < 60) {
    console.log(`A usuária ${nomeCompleto} é adulta.`);
  } else if (idade >= 60) {
    console.log(`A usuária ${nomeCompleto} é idosa.`);
  } else {
    console.log(`A usuária ${nomeCompleto} é menor de idade.`);
  }
  
//verificar se é maior de idade (de forma com if e else) <--
var nome =  'Ada';
var sobrenome = 'Lovelace';
var nomeCompleto = nome + ' ' + sobrenome;
var idade = 36;
  
    if (idade >= 18) {
      alert(`A usuária ${nomeCompleto} é adulta.`);
    } else {
      alert(`A usuária ${nomeCompleto} é menor de idade.`);
    }

// com vários else if
if (a === 0) {
    alert('zero');
} else if (a === 1) {
    alert('um');
} else if (a === 2) {
    alert('dois');
} else if (a === 3) {
    alert('três');
} else {
    alert('diferente de 0, 1, 2 e 3');
}

//Outro modo de testar e outro modo de escrever os if e else
var num = 0
switch (num) {   // usado só para funções exatas, usado quando você sabe exatamente qual pode ser o resultado (não funciona por exemplo com > ou < )
    case 0:
      alert('zero');
      break;   // Deve ser usado um break para parar a repetição, pois se não tiver ele, mesmo sendo o resultado esperado, ele vai continuar executando os demais.
    case 1:
      alert('um');
      break;
    case 2:
      alert('dois');
      break;
    case 3:
      alert('três');
      break;
    default:   // ele é o último a ser executado como se fosse um else (então ele vai parar as repetições).
      alert('diferente de 0, 1, 2 e 3');