<template>

    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
            <div class="modal-header">

                <h5 class="modal-title" id="exampleModalLabel">Preencha os campos abaixo:</h5>
                <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <!-- formulário para capturar os dados -->
                <form class="formulario" @submit.prevent="salvarMovimento">  
                    <div class="form-group">
                            <label for="exampleInputEmail1">Nome</label>
                            <Field type="email" class="form-control" id="nome" name="nome" v-model="movimentacao.nome" placeholder="Ex: Batata" :rules="validacao.validarCampos" />
                            <span>
                                <ErrorMessage name="nome"/>
                            </span>
                        </div>
                        <div class="form-group">
                            <label for="exampleInputPassword1">Valor</label>
                            <Field type="number" class="form-control" id="valor" name="valor" v-model="movimentacao.valor" placeholder="R$" :rules="validacao.validarValor" />
                            <ErrorMessage name="valor"/>
                        </div>
                        <div class="form-group">
                            <label for="exampleInputPassword1">Informações</label>
                            <Field type="text" class="form-control" id="info" name="info" v-model="movimentacao.info" placeholder="Descrição do item" :rules="validacao.validarCampos" />
                            <ErrorMessage name="info"/>
                        </div>
                        
                        <div class="form-group">
                            <label for="exampleInputPassword1">Data</label>
                            <Field type="date" class="form-control" id="data" name="data" v-model="movimentacao.data" placeholder="Escolha uma"/>
                            <ErrorMessage name="data"/>
                        </div>
                        <div class="form-group">
                            <label for="tipo">Tipo de dado</label>
                            <Field class="form-select" name="tipo" as="select" :rules="validacao.validarCampos" />
                                <option selected disabled>Selecione uma opção</option>
                                <option v-for="tipo in tipos" :key="tipo" :value="tipo">{{ tipo }}</option>
                                <ErrorMessage name="tipo    "/>
                        </div>

                    <!-- botões de ação -->
                    
                </form>
                </div>
                 <div class="modal-footer">
                    <button type="submit" class="btn btn-success btn-add" :disabled="habilitaBtn" >Adicionar</button>
                    <button  type="button" data-bs-dismiss="modal" class="btn btn-danger btn-add">Cancelar</button>
                </div>
            </div>
        </div>
    </div>


</template>

<script>
import { Form, Field, ErrorMessage } from 'vee-validate'
import ValidacaoV from '../validacaoV'

export default {
    name: 'ComponenteModal',
    data(){
        return {
            
            movimentacao: {
                nome: null,
                valor: null,
                info: null,
                data: null,
                tipo: null,

            },
            validacao: null,
            tipos: null,
            lista: []
        }
    },
    computed: {
        habilitaBtn(){
            return this.movimentacao.nome && this.movimentacao.valor && this.movimentacao.info && this.movimentacao.data && this.movimentacao.tipo
        }
    },
    components:{
        Form,
        Field,
        ErrorMessage,
        ValidacaoV
       
    },
    beforeMount() {
        this.tipos = ['Entradas', 'Saídas']
      
        this.validacao = ValidacaoV;
    },

    methods: {
        salvarMovimento() {
            this.$emit('movimentacaoSalva', this.movimentacao)
            this.limparCampos() 
        },
        limparCampos(){
            this.movimentacao.nome = null
            this.movimentacao.valor = null
            this.movimentacao.info = null
            this.movimentacao.data = null
            this.movimentacao.tipo = null
        }
        
    }
}

</script>

<style>


</style>