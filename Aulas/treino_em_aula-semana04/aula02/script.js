console.log('funciona?');

class Carro {
    constructor(marca, modelo, ano, fipe, valoPago){
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.fipe = fipe;
        this.valorPago = valoPago;
    }
    venda(){
        //método/função para comparar o valor com a fipe
        if (this.fipe > this.valorPago){
            console.log(`Esse ${this.modelo} está em um preço bom para revender.`)
        } else if (this.fipe == this.valorPago){
            console.log(`Esse ${this.modelo} está no mesmo valor da fipe, tente melhorar.`)
        } else{
            console.log(`Esse ${this.modelo} não está em um preço bom para revender.`)
        }
        
    }
    
}

const gol = new Carro("Wolksvagem", "Gol 1.0", 2011, 25000, 23000);
gol.venda(); //chama a função venda que vai printar no console o que foi resolvido no if else


class Endereco{
    constructor(logradouro, numero, ciade, estado, pais, cep){
        this.logradouro = logradouro;
        this.numero = numero;
    }
    rua(){
        console.log(`Sua rua é ${this.logradouro} e seu número é ${this.numero}.`);
    }
}

const marcos = new Endereco("Rua Paraíba", 345, "Pérola", "PR", "Brasil", 85740000);
marcos.rua();



/****************************************************************************/
//Exercício de grupo em aula 

class Veiculo {
    constructor(tipoVeiculo, marca, modelo, ano, placa, numMultas, velocidadeMaxima) {
        this.tipoVeiculo = tipoVeiculo;
        this.marca = marca;
        this.modelo = modelo;
        this.ano = ano;
        this.placa = placa;
        this.numMultas = numMultas;
        this.velocidadeMaxima =velocidadeMaxima;
    }

    getTipoModelo(){
    return `Carro tipo: ${this.tipoVeiculo}, modelo: ${this.modelo}`;
    }
    adicionaMulta(placa){
        if(placa == this.placa){
            this.numMultas++
            console.log(`Número de multas ${this.numMultas}.`);
        }
        else{
            console.log('Placa inválida');
        }

    }
}

const bmwX5 = new Veiculo('Esportivo','BMW','x5','2019','AAA-0000', 3,300);

bmwX5.adicionaMulta('AAA-0000');

console.log(bmwX5.getTipoModelo());

bmwX5.adicionaMulta('AAA-000');