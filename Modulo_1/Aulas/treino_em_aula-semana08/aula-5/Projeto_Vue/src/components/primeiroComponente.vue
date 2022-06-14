<template>
<div>
    <div class="msg-tabela" v-if="movimentacoes.length == 0">
        <h5 v-text="msg_tabela"></h5>
    </div>
    <!-- Montagem da tabela -->
    <table class="table table-striped">
        <thead>
            <th>indice</th>
            <th>Nome</th>
            <th>Valor</th>
            <th>Informações</th>
            <th>Data</th>
            <th>Tipo</th>
            <th>Ações</th>
            
            </thead> 
            <tbody v-for="(item, indice) in movimentacoes" :key="indice">
                <th>{{indice + 1}}</th>
                <th>{{item.nome}}</th>
                <th> R$ {{item.valor}}</th>
                <th>{{item.info}}</th>
                <th>{{item.data}}</th>
                <th>{{item.tipo}}</th>
                <th>
                    <!-- botões de ação para cada item -->
                    <button class="btn-acao" type="button" @click="editar(indice)">Editar</button>
                    <button class="btn-acao" type="button" @click="deletaProduto(indice)">Excluir</button>
                </th>
            
            </tbody>
    </table>
</div>       
</template>

<script>
export default {
    name: 'primeiroComponente',
    data(){
        return {
            
            movimentacao: {
                nome: null,
                valor: null,
                info: null,
                data: null,
                tipo: null,

            },
            msg_tabela: 'Clique no botão para começar a lista',
            movimentacoes: []
        }
    },
    methods: {
        adicionarMovimento(){
            
        },
        
        
        //irá ser adicionado a função EDITAR aqui   
        
        excluirMovimentacao() {
            this.$emit('excluirMovimentacao', this.movimentacoes);
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