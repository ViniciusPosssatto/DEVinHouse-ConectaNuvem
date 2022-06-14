// MODO PÚBLICO

/*class Pessoa {
    constructor (nome, idade) {
        this.nome = nome;
        this.idade = idade;
    }

    caminhar(){
        return `${this.nome} está caminhando!`
    }
    exibir(){
        return `Meu nome é ${this.nome} e tenho ${this.idade} anos.`
    }
}

var pessoa1 = new Pessoa ("Ana", 29);
console.log(pessoa1.nome);
console.log(pessoa1.caminhar());
console.log(pessoa1.exibir());
*/

/*///////////////////////////////*/

// MODO PRIVADO
/*
class Pessoa {
    #nome
    #idade

    constructor (nome, idade) {
        this.#nome = nome;
        this.#idade = idade;
    }

    get nome(){
        return this.#nome;
    }

    set nome(nome){
        this.#nome = nome;
    }

    get idade(){
        return this.#idade;
    }

    set idade(idade){
        this.#idade = idade;
    }

    caminhar(){
        return `${this.#nome} está caminhando!`;
    }
    exibir(){
        return `Meu nome é ${this.#nome} e tenho ${this.#idade} anos.`;
    }
}

var pessoa1 = new Pessoa ("Ana", 29);
console.log(pessoa1.nome);

pessoa1.nome = "Marcelo"; //substitui Ana por Marcelo a partir de agora 
console.log(pessoa1.nome);

console.log(pessoa1.caminhar());
console.log(pessoa1.exibir()); //substituiu o nome porém continuou a idade dela...


*/

/*///////////////////////////////////*/

//Closure
/*
let x = 50;

function somarMais3(){
    return x + 3;
}

module.exports = somarMais3;
*/

////////////////////////////////////////////////

// HERANÇA
/*
class Dev {
    constructor(nome, idade, principalLinguagem){
        this.nome = nome;
        this.idade = idade;
        this.principalLinguagem = principalLinguagem;
    }

    apresentacao(){
        console.log(`Sou dev, trabalho com ${this.principalLinguagem}, meu nome é ${this.nome} e tenho ${this.idade}.`)
    }
}

//const dev = new Dev("Andrei", 40, "Python");
//dev.apresentacao();

class FrontendDev extends Dev{
    constructor(nome, idade, principalLinguagem, framework){   //mesmo que sejam os mesmos itens da classe mãe, tem que ser defnido novamente aqui.
        super();  // puxa os itens da classe mãe
        this.framework = framework;
    }

    apresentacao(){
        console.log(`Sou frontend, trabalho com ${this.framework}, mas também utilizo ${this.principalLinguagem}, meu nome é ${this.nome} e tenho ${this.idade}.`)
    }
}

const front = new FrontendDev("Ana", 32, "python", "HTML5");
front.apresentacao();
*/

/////////////////////////////////////////////////////////////

// POLIMORFISMO

class Pessoa{
    ser(){
    console.log("Eu sou uma pessoa.")
    }
}

class Jovem extends Pessoa{}

//const pessoa = new Pessoa;
//pessoa.ser();

class Idoso extends Pessoa{
    ser(){   // modifica a mensagem da função ser que vem lá da class mãe
        console.log("Eu sou um idoso, pois tenho idade avançada!");
    }
}

const pessoa = [new Pessoa(), new Jovem()];  // montado um array com 2 new 
pessoa.forEach(pessoa => pessoa.ser()); // forEach percore os 2 itens do array e apresenta na tela a função ser de cada um

const idoso = new Idoso;
idoso.ser();





