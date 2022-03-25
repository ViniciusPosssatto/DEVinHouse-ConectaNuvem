class Conta{
  constructor(numeroConta, saldo, cliente){
    this.numeroConta = numeroConta;
    this.saldo = saldo;
    this.cliente = cliente;
  }

  verificarSaldo(){
    if(this.saldo >= 1){
      return `O saldo em conta do Sr(a) ${this.cliente} é de R$${this.saldo}.`
    } else{
      return `O Sr(a) não possui saldo ativo em conta.`
    }
  }
}

const cliente1 = new Conta(23475-0, 400.344, 'Josemar Lopez');
console.log(cliente1.verificarSaldo());