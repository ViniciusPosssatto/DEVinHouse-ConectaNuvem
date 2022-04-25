<template>
<div>
    
    <!-- <div class="msg-tabela" v-if="this.lista.length == 0">
        <h5 v-text="msg_tabela"></h5>
    </div> -->
    <!-- Montagem da tabela -->
    <table class="table table-striped" v-if="listas.length > 0">
        <thead>
            <th>indice</th>
            <th>Nome</th>
            <th>Qauntidade</th>
            <th>Valor</th>
            <th>Ações</th>
            
        </thead> 
            <tbody v-for="(item, indice) in listas" :key="indice">
                <th>{{indice + 1}}</th>
                <th>{{item.nome}}</th>
                <th>{{item.qtdade}}</th>
                <th> R$ {{item.valor}}</th>
                <th>
                    <!-- botões de ação para cada item -->
                    <button class="btn-acao" type="button" @click="editar(indice)">Editar</button>
                    <button class="btn-acao" type="button" @click="excluirProduto(indice)">Excluir</button>
                </th>
            
            </tbody>
    </table>
    <span v-else>Clique no botão para comçar sua lista!</span>
    
</div>       
</template>

<script>
export default {
name: 'primeiroComponente',
    props: {
        listas: {
            type: Array,
            require: true,
            default: null
        }
    },
    
    methods: {
        adicionaProduto(){
            this.$emit('adicionaProduto', this.lista)
        },
        excluirProduto(indice) {
            this.listas.splice(indice, 1);
        },
        limparLista() {
            this.$emit('limparLista', this.listas)
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