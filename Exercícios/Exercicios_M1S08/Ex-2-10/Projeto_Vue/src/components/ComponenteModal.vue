<template>

    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
            <div class="modal-header">

                <h5 class="modal-title" id="exampleModalLabel">Preencha os campos abaixo:</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <!-- formulário para capturar os dados -->
                <form class="formulario">  
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
            </div>
            <div class="modal-footer">

                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>


            </div>
        </div>
    </div>
    </div>


</template>

<script>
export default {
    name: 'ComponenteModal',
    data(){
        return {
            
            produtos: {
                nome: null,
                valor: null
            },
            mensagemErro: null,
            erroNome: false,
            erroValor: false,
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
    }
}

</script>

<style>


</style>