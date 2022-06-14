class Cliente {
    constructor(){
        this.id = 0;
        this.arrayClientes = [];
    }
    salvar() {
        let cliente1 = this.lerDados();

        if (this.validaCampo(cliente1)) {
            alert('salvar');
        }

        console.log(cliente1);
    }
    lerDados() {
        let cliente1 = {}

        cliente1.id = this.id;
        nome.nomeCliente = document.getElementById("nome").value;
        cpf.cpfCliente = document.getElementById("cpf").value;

        return cliente1;
    }

    validaCampo(cliente1) {
        let msg = '';

        if (nome.nomeCliente == '') {
            msg += 'Informe o seu nome completo! ';
        }

        if (cpf.cpfCliente == '' || cpf.cpfCliente.length !== 11){
            msg += 'Informe o número do CPF correto! ';
        }

        if (msg != '') {
            alert(msg);
            return false;
        }

        return true;
    }
}

var cliente1 = new Cliente();