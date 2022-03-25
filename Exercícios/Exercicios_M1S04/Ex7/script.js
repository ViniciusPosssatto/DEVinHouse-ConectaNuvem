//capturar os dados do Html
var resultado = document.getElementById('resultado');
//var botao = document.getElementById('botao');
var imagens = document.getElementById('estacoes');

//declarar as datas atuais e separá-las
var dataAtual = new Date();
var anoAtual = dataAtual.getFullYear();
console.log(anoAtual);
var mesAtual = dataAtual.getMonth() + 1;
console.log(mesAtual);
var diaAtual = dataAtual.getDate();
console.log(diaAtual);

// Definir as datas do Verão
var veraoI = new Date("2021/12/22")
var veraoF = new Date("2022/3/21")

// Definir as datas do Outono
var outonoI = new Date("2022/3/22")
var outonoF = new Date("2022/6/21")

// Definir as datas do Inverno
var invernoI = new Date("2022/6/22")
var invernoF = new Date("2022/9/21")

// Definir as datas da Primavera
var primaveraI = new Date("2022/9/22")
var primaveraF = new Date("2022/12/21")

console.log(veraoI, veraoF);

//organizar os 3 elementos que separamos para poder comparar com as datas acima
var corrigeDate = new Date(`${anoAtual}/${mesAtual}/${diaAtual}`);

console.log(corrigeDate);

function verificar () {
  if (corrigeDate >= veraoI && corrigeDate <= veraoF) {
    resultado.innerText = "Estamos no verão, que calor!!"
    imagens.src = "verao.jpg"
    console.log('verão');

  } else if (corrigeDate >= outonoI && corrigeDate <= outonoF) {
    resultado.innerText = "Estamos no outono, quantas folhas caindo."
    imagens.src = "outono.jpg"
    console.log('Outono');

  } else if (corrigeDate >= invernoI && corrigeDate <= invernoF) {
    resultado.innerText = "Estamos no Inverno, que friiio..."
    imagens.src = "inverno.jpg"
    console.log('Inverno');

  } else {
    resultado.innerText = "Estamos na primavera, época das flores."
    imagens.src = "primavera.jpg"
    console.log('Primavera');
  }
};