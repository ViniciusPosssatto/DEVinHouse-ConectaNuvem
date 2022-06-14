// const express = require('express');
// const app = express();
// const port = 8081;

// app.get('/', (req, resp) => {
//     resp.send('Hello, world!');
// });

// app.listen(port, () => {
//     console.log(`Essa aplicação está rodando na porta ${port}`)
// })

// const readLine = require('readLine');

// let nome = readLine.question('Insira seu nome');

// console.log(nome);


    var opcao = '';
    
do{

    var readLineSync = require('readline-sync');

    console.log('Vamos descobrir seu IMC!');

    var peso = readLineSync.question('informe o seu peso: ');
    var altura = readLineSync.question('informe a sua altura: ')

    function calculaIMC(pesoInformado, alturaInformada){
        const IMC = pesoInformado/(alturaInformada*alturaInformada);

        if (IMC <18.5){
            return `Você está abaixo do peso - IMC de ${IMC.toFixed(2)}`
        } else if(IMC >= 18.5 && IMC < 25){
            return `Você está com peso normal - IMC de ${IMC.toFixed(2)}`
        }else if(IMC >= 25 && IMC < 30){
            return `Você está com sobrepeso - IMC de ${IMC.toFixed(2)}`
        }else if(IMC >= 30 && IMC < 35){
            return `Você está com obesidade grau I - IMC de ${IMC.toFixed(2)}`
        }else if(IMC >= 35 && IMC < 40){
            return `Você está com obesidade grau II - IMC de ${IMC.toFixed(2)}`
        }else if(IMC > 40){
            return `Você está com obesidade grau III - IMC de ${IMC.toFixed(2)}`
        }
    }

    console.log(calculaIMC(peso, altura));

    opcao = readLineSync.question("Deseja constinuar? s ou n = ");

    if(opcao == "s"){
        continue
    }else if(opcao == "n"){
        break
    }else{
        console.log("Opção inválida.")
    }
} while (opcao == "s");

