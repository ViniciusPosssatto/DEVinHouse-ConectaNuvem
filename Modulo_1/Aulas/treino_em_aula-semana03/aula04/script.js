function falaOi() {
    console.count('Oi!');
}

setTimeout(falaOi, 2000);
var timeoutOi = setTimeout(falaOi, 3000);
clearTimeout(timeoutOi); //zerando o timeout

setInterval(falaOi, 1000);
var intervalOi = setInterval(falaOi, 1000);
clearInterval(falaOi); //zerando o interval

//colocando a função dentro do set timeout
setTimeout(function () {
    console.log('Limpando interval.')
    clearInterval(intervalOi);
}, 4000); //executa o clear após 4 segundos

//fazendo a contagem dos intervalos e interrompendo
// var i = 1;
// var intervalOi = setInterval(function () {
//   falaOi();
//   i++;
//   if (i > 3) {  //interrompe o interval quando o i for maior que 3 vzs
//     clearInterval(intervalOi);
//   }
// }, 1000);

//contador até 10
var conta = 0
var meutimeout = setInterval(() => {
    console.log("Olá"+conta)
    conta++
    if(conta == 10){
        clearTimeout(meutimeout)
    }
}, 1000)

