const arrayNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9];

//função array que eleva o número na potência 2 e cria um novo array com os resultados
let arrayQuadrados = arrayNumeros.map(num => num ** 2);

//exibe o novo array  a partir do map
console.log(arrayQuadrados)

//fuinção array que verifica quais itens são maiores que 30 e cria um novo array com eles
let maiorQue = arrayQuadrados.filter(num => num >= 30);

//Exibe o novo array a partir do filter
console.log(maiorQue);