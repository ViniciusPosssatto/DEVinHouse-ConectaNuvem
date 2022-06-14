<template>
    <div class="container">
        <form class="formulario">  <!-- formulário para capturar os dados -->
            <div id="container">
                <div class="mb-3">
                    <label class="form-label" for="nome-produto">Digite o nome do produto:</label>
                    <input class="form-control" id="produto" type="text" v-model="produtos.nome" placeholder="Ex: batata" />
                    <span v-if="erroNome" class="msg-erro">{{ mensagemErro }}</span>
                </div>
                <div class="mb-3">
                    <label class="form-label" for="valor-produto">Digite o valor do produto:</label>
                    <input class="form-control" id="valor" type="number" v-model="produtos.valor" placeholder="R$: " />
                    <span v-if="erroValor" class="msg-erro">{{ mensagemErro }}</span>
                </div>
            </div> <!-- botões de ação -->
            <button @click.prevent="submit()" class="btn btn-success btn-add">Adicionar</button>
            <button @click.prevent="cancelar()" class="btn btn-danger btn-add">Cancelar</button>
        </form>
        <div>
            <div class="msg-tabela" v-if="lista.length == 0">
                <h5 v-text="msg_tabela"></h5>
            </div>
            <!-- Montagem da tabela -->
            <table class="table table-striped">
                <thead>
                    <th>indice</th>
                    <th>Nome</th>
                    <th>Valor</th>
                    <th>Ações</th>
                    
                    </thead> 
                    <tbody v-for="(item, indice) in lista" :key="indice">
                        <th>{{indice + 1}}</th>
                        <th>{{item.nome}}</th>
                        <th> R$ {{item.valor}}</th>
                        <th>
                            <!-- botões de ação para cada item -->
                            <button class="btn-acao" type="button" @click="editar(indice)">Editar</button>
                            <button class="btn-acao" type="button" @click="deletaProduto(indice)">Excluir</button>
                        </th>
                    
                    </tbody>
            </table>
              
        </div>
        
    </div>
</template>

<script>
export default {
    name: 'primeiroComponente',
    data(){
        return {
            
            produtos: {
                nome: null,
                valor: null
            },
            mensagemErro: null,
            erroNome: false,
            erroValor: false,
            msg_tabela: 'Coloque um produto para começar a lista',
            lista: []
        }
    },
    methods: {
        submit() {
            if (this.validar(this.produtos)){
                this.lista.push({
                    nome: this.produtos.nome,
                    valor: this.produtos.valor
                })
            }
            
        },
        
        //irá ser adicionado a função EDITAR aqui   

        validar(produtos) {
            if(!produtos.nome) {
                this.mensagemErro = 'Preencha o campo nome produto!'
                this.erroNome = true
                return false
            } else if (!produtos.valor) {
                this.mensagemErro = 'Do valor também!'
                this.erroNome = true
                return false
            }
            return true;
        },

        cancelar(){
            this.produtos.nome = '';
            this.produtos.valor = '';
        },
        deletaProduto(indice) {
            this.lista.splice(indice, 1);
        }
    
    }

}
</script>

<style scoped>
*{
    font-family: Verdana, Geneva, Tahoma, sans-serif;
}
form{
    display: flex;
    flex-direction: column;
    margin: 0 auto;
    margin-bottom: 15px;
}
.btn-add{
    margin: 10px 0;
    width: 150px;
    align-content: center;
    align-items: center;
}
.btn-acao{
    margin: 0 10px;
    color: aqua;
    cursor: pointer;
    transition: all 0.5s;
}
.btn-acao:hover{
    -webkit-transform: scale(1.5);
    transform: scale(1.2);
    background-color: brown;
}
table{
    align-content: center;
    align-items: center;
    background-color: rgb(55, 56, 56);
    color: white;
    padding: 20px;
    text-align: center;
}
.formulario{
    display: flex;
    flex-direction: column;
    align-content: center;
    align-items: center;
    margin: 20px 20px;
}
.msg-erro{
    color: rgb(164, 5, 5);
}
.msg-tabela{
    color: rgb(222, 12, 12);
    text-align: center;
    padding: 5px;
    margin-bottom: 15px;
    background-color: black;
    margin-left: auto;
    margin-right: auto;
}
thead{
    background-color: rgb(8, 6, 6);
}
</style>

<style>
body{
    background-color: rgb(163, 165, 165);
}
</style>