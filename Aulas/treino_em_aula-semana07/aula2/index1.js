
// do{
//     var readLine = require('readline-sync')
//     const pi = 3.14;
//     var opcao = "";

//     console.log("Bem-vindo ao calculador de área!!! \n 1 - Circulo \n 2 - Quadrado \n 3 - Retangulo \n 4 - Triangulo \n 5 - Exit")
   
//     var opcao = readLine.question("Digite sua opcao: ")

//     switch (opcao) {
//         case 1:
//             calculoCirculo()
//                 raio = readLine.question('informe o raio da circunferencia: ');
//                 result = pi * (raio ** 2);
//                 console.log(`A área do círculo é ${result.toFixed(2)}`);
//         case 2:
//             console.log(calculoQuadrado());
        
//         case 3:
//             console.log(calculoRetangulo());
        
//         case 4:
//             console.log(calculoTriangulo());
        
//         case 5:
//             break;
//         }   
    
// }while (opcao != 5)




// calculoQuadrado()
//     lado = readLine.question('informe o valor do lado do quadrado: ');
//     result = lado **2;
//     console.log(`A área do quadrado é ${result.toFixed(2)}`);

// calculoRetangulo()
//     lado = readLine.question('Digite o valor da base do retângulo: ');
//     otoLado = readLine.question('Digite a altura do retângulo: ');
//     result = lado * otoLado
//     console.log(`A área do retângulo é ${result.toFixed(2)}`);

// calculoTriangulo()
//     base = readLine.question('Infome a largura da base do triângulo: ');
//     altura = readLine.question('Infome a altura do triângulo: ');
//     result = (base * altura) / 2;
//     console.log(`A área do triângulo é ${result.toFixed(2)}`);

////////////*/////////////////////*//////////////////*///////////////////*////////

var readLine = require('readline-sync')
const pi = 3.14;
var opcao = true;

    console.log("Bem-vindo ao calculador de área!!! ")
   while(opcao === true) {
       calcula = ['circulo', 'quadrado', 'retângulo', 'triângulo', 'exit'],
       tipo = readLine.keyInSelect(calcula, 'Escolha o numero correspondente a figura: ');

       if(tipo === 0){
            raio = readLine.question('informe o raio da circunferencia: ');
            result = pi * (raio ** 2);
            console.log(`A área do círculo é ${result.toFixed(2)} cm2`);
       } else if (tipo === 1){
            lado = readLine.question('informe o valor do lado do quadrado: ');
            result = lado **2;
            console.log(`A área do quadrado é ${result.toFixed(2)} cm2`);
       } else if(tipo === 2){
            lado = readLine.question('Digite o valor da base do retângulo: ');
            otoLado = readLine.question('Digite a altura do retângulo: ');
            result = lado * otoLado
            console.log(`A área do retângulo é ${result.toFixed(2)} cm2`);
       } else if(tipo === 3){
            base = readLine.question('Infome a largura da base do triângulo: ');
            altura = readLine.question('Infome a altura do triângulo: ');
            result = (base * altura) / 2;
            console.log(`A área do triângulo é ${result.toFixed(2)} cm2`);
       } 
   }