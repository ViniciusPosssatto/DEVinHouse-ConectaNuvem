class Cliente{
    constructor(nome, cpf, endereco, numeroCelular){
        this.nome = nome;
        this.cpf = cpf;
        this.endereco = endereco;
        this.numeroCelular = numeroCelular;
    }

    contato(){
        return `Para maiores informações falar com ${this.nome} no número ${this.numeroCelular}.`
    }
}

const pessoa = new Cliente('Maxson', 04598345523, 'Rua Euclides, 3445, ap 13', 4599455323);
console.log(pessoa.contato());