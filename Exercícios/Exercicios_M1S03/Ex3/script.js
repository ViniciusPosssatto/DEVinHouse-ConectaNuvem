function calcular(){
    
    var tn1 = window.document.getElementById('txtn1');
    var tn2 = window.document.getElementById('txtn2');
    

//outra forma de chamar o valor do imput ja convertido em numero(sen precisar converter em outra var abaixo).
/*
    var tn1 =  Number(document.getElementById('txtCalc1').value);
    var tn2 = Number(document.getElementById('txtCalc2').value);
*/

    var operacao = window.document.getElementById('operacao');
    var resultado = window.document.getElementById('resultado');

    var num1 = Number(tn1.value);
    var num2 = Number(tn2.value);

    var operador = operacao.value;
    
    if (operador == 'adicao'){
        var result = num1 + num2;
    }
    if (operador == 'subtracao'){
        var result = num1 - num2
    }
    if (operador == 'multiplicacao'){
        var result = num1 * num2
    }
    if (operador == 'divisao'){
        var result = num1 / num2
    }

    resultado.innerHTML = `A ${operador} entre ${num1} e ${num2} é igual a ${result}.`;
}
