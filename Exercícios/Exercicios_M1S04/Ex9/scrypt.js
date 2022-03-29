//transações pix

class Transacao{
    #valorConta
    #valorDaTransacao
    constructor(valorConta, valorDaTransacao){
        this.#valorConta = valorConta;
        this.#valorDaTransacao = valorDaTransacao;
    }
    get saldoEmConta() {
        return this.#valorConta
    }
    get saldoTransacao() {
        return this.#valorDaTransacao
    }

    transferencia(){
        let desconta = this.saldoEmConta - this.saldoTransacao;
        if (this.saldoEmConta < 0 || this.saldoEmConta < this.saldoTransacao){
            console.log('Você não possui saldo em conta, suficiente para o pagamento deste item.')
            console.log(`Saldo disponível = R$${this.saldoEmConta}`);
        } else if (this.saldoEmConta >= this.saldoTransacao){
            console.log('Sua transação foi efetuada.');
            console.log(`Saldo disponível = R$${desconta}`);
        }
    }
    deposito(){
        let soma = this.saldoEmConta + this.saldoTransacao;
        return console.log(`Você recebeu um pix no valor de R$${this.saldoTransacao}, seu saldo agora é de R$${soma}.`);
    }
}


const cliente1 = new Transacao(3000, 380)

//quando faz pagamento com pix
cliente1.transferencia();
//quando recebe pagamentos de pix
cliente1.deposito();