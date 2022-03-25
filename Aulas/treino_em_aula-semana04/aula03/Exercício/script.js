class Produto {
    constructor(){
        this.id = 0;
        this.arrayProdutos = [];
    }

    salvar() {
        let produto = this.lerDados();

        if (this.validaCampo(produto)) {
            alert('salvar');
        }

        console.log(produto);
    }

    cancelar() {
    }

    lerDados() {
        let produto = {}

        produto.id = this.id;
        produto.nomeProduto = document.getElementById("produto").value;
        produto.valorProduto = document.getElementById("valor").value;

        return produto;
    }

    validaCampo(produto) {
        let msg = '';

        if (produto.nomeProduto == '') {
            msg += 'Informe um nome de produto! ';
        }

        if (produto.valorProduto == '') {
            msg += 'Informe um valor para o produto! ';
        }

        if (msg != '') {
            alert(msg);
            return false;
        }

        return true;
    }
}

var produto = new Produto();