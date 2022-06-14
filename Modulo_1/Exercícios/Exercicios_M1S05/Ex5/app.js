const soma = document.getElementById('rest');

import produto from "./utils.js";

const resutado = produto(14, 24, 33, 46, 51, 67, 71, 83, 98);

//imprime na tela
soma.innerHTML = `Soma de todos os números = ${resutado}.`;
//imrpime no console
console.log(resutado);