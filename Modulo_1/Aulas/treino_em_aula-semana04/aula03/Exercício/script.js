class Produto{
    constructor(){
        this.id = 1;
        this.arrayProdutos = [];

    }

    salvar(){
        let produto = this.lerDados();

        if(this.validaCampos(produto)){
            this.adicionar(produto);
        }

        this.listaTabela();

    }

    listaTabela(){

        let tbody = document.getElementById('tbody');

        tbody.innerText = '';

        for(let i = 0; i < this.arrayProdutos.length; i++) {

        let tr = tbody.insertRow();

        let td_id = tr.insertCell();
        let td_produto = tr.insertCell();
        let td_valor = tr.insertCell();
        let td_acoes = tr.insertCell();

        td_id.innerText = this.arrayProdutos[i].id;
        td_produto.innerText = this.arrayProdutos[i].nomeProduto;
        td_valor.innerText = this.arrayProdutos[i].valor;

        let imgEdit = document.createElement('img');
        imgEdit.src="./img/editar.jpg";

        td_acoes.appendChild(imgEdit);

        let imgDelete = document.createElement('img');
        imgDelete.src="./img/deletar.jpg";

        td_acoes.appendChild(imgDelete);
        }
    }

    adicionar(produto){

        this.arrayProdutos.push(produto);
        this.id++;
    }

    lerDados(){
        let produto = {}

        produto.id = this.id;
        produto.nomeProduto = document.getElementById('produto').value;
        produto.valor = document.getElementById('valor').value;

        return produto;

    }

    validaCampos(produto){
        let msg = '';

        if(produto.nomeProduto == ''){
            msg += ' - Informe o nome do Produto \n';
        }

        if(produto.valor == ''){
            msg += ' - Informe o valor do Produto \n';
        }

        if(msg != ''){
            alert(msg);
            return false;
        }

        return true;
    }

    cancelar(){
        alert('Item cancelado')
    }
}

var produto = new Produto();