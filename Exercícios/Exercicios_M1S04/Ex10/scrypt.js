//transações pix

class Transacao{
    valorConta
    valorDaTransacao
    idTransacao = 1;
    contaDestino
    data
    agencia
    constructor(valorConta, valorDaTransacao){
        this.valorConta = valorConta;
        this.valorDaTransacao = valorDaTransacao;
    }
    getsaldoEmConta() {
        return this.valorConta
    }
    getsaldoTransacao() {
        return this.valorDaTransacao
    }

    getidTransacao(){
        return this.idTransacao++;
    }
    setidTransacao(){
        this.idTransacao++
    }

    getData(){
        return this.data;
        
    }
    setData(){
        var data = new Date()
        var dia = data.getDate()
        var mes = data.getMonth() + 1
        var ano = data.getFullYear()
        var hora = data.getHours()
        var minutos = data.getMinutes()

        this.data = `${dia}/${mes}/${ano} - ${hora}:${minutos}`
    }

    getcontaDestino(){
        return this.contaDestino
    }

    setcontaDestino(numero){
        this.contaDestino = numero
    }
    getagenciaDestino(){
        return this.agenciaDestino
    }

    setagenciaDestino(numero){
        this.agenciaDestino = agencia
    }

    transferencia(contaDestino,){
        let desconta = this.getsaldoEmConta() - this.getsaldoTransacao();

        if (this.getsaldoEmConta() < 0 || this.getsaldoEmConta() < this.getsaldoTransacao()){

            this.getidTransacao()
            this.contaDestino
            this.data
            
            console.log('Você não possui saldo em conta, suficiente para o pagamento deste item.')
            console.log(`Saldo disponível = R$${this.getsaldoEmConta()}`);

        } else if (this.getsaldoEmConta() >= this.getsaldoTransacao()){

            console.log(`Sua transação de número ${this.getidTransacao()} foi efetuada.`);
            console.log(`O valor de R$${this.getsaldoTransacao()} foi enviado para a conta ${contaDestino} na data de ${this.data}.`)
            console.log(`Saldo disponível = R$${desconta}`);
        }
    }
    deposito(){
        
        this.getidTransacao()
        this.contaDestino
        this.getData()

        let soma = this.getsaldoEmConta() + this.getsaldoTransacao();
        return console.log(`Você recebeu um pix no valor de R$${this.getsaldoTransacao()} (transação nº ${this.getidTransacao()}) em ${this.getData()}, seu saldo agora é de R$${soma}.`);
    }
}

console.log(this.data);
const cliente1 = new Transacao(3000, 380)

//teste 1 para a contagem de transações
cliente1.transferencia('4233-3');
//teste 2 para a contagem de transações
cliente1.transferencia('3435-2')

//quando faz pagamento com pix
//cliente1.transferencia();
//quando recebe pagamentos de pix
//cliente1.deposito();
