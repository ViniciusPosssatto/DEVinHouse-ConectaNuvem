const pessoa = document.getElementById('pessoa');

import Pessoa from "./Pessoa.js";


const p1 = new Pessoa('Marcos', 33455566);

//imprime na tela
pessoa.innerHTML = p1.imprime();
//imrpime no console
console.log(p1.imprime())