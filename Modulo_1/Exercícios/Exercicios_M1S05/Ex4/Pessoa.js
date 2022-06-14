

class Pessoa{
    #cpf
    constructor(nome, cpf){
        this.nome = nome;
        this.#cpf = cpf;
    }

    get cpf(){
        return this.#cpf
    }

    imprime(){
        return `O seu nome é ${this.nome} e o seu CPF é ${this.#cpf}.`;
    }
}

export default Pessoa;

