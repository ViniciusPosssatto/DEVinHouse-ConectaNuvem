<template>

    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">

                    <h5 class="modal-title" id="exampleModalLabel">Adicione um item a lista:</h5>
                    <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <!-- formulário para capturar os dados -->

                    <Form @submit="salvarProduto">  
                        <div class="form-group">
                            <label for="nome">Nome</label>
                            <Field type="text" class="form-control" id="nome" name="nome" v-model="produtos.nome" placeholder="Ex: Batata" :rules="validacao.validarCampos" />
                            <span class="error-message">
                                <ErrorMessage name="nome" />
                            </span>
                        </div>
                        <div class="form-group">
                            <label for="qtdade">Quantidade</label>
                            <Field type="number" class="form-control" id="qtdade" name="qtdade" v-model="produtos.qtdade" placeholder="" :rules="validacao.validarCampos" />
                            <span class="error-message">
                                <ErrorMessage name="qtdade" />
                            </span>
                        </div>
                        <div class="form-group">
                            <label for="valor">Valor</label>
                            <Field type="number" class="form-control" id="valor" name="valor" v-model="produtos.valor" placeholder="R$" :rules="validacao.validarCampos" />
                            <span class="error-message">
                                <ErrorMessage name="valor" />
                            </span>
                            
                        </div>
                    </Form>  
                </div> 
                <!-- botões de ação --> 
                <div class="modal-footer">
                    <button type="submit" data-bs-dismiss="modal" @click="salvarProduto" :disabled="habilitarBtn" class="btn btn-success btn-add">Adicionar</button>
                    <button class="btn btn-danger btn-add" data-bs-dismiss="modal">Cancelar</button>
                    
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
                
                produtos: {
                    nome: null,
                    qtdade: null,
                    valor: null
                },
                validacao: null,
            }
        },
        computed: {
            habilitarBtn(){
                return this.nome && this.qtdade && this.valor
            }
        },
        components:{
            Form,
            Field,
            ErrorMessage,
            ValidacaoV
        
        },
        beforeMount() {
            this.validacao = ValidacaoV;
            //console.log(ValidacaoV)
        },
        methods: {
        
            salvarProduto() {
                this.$emit('produtoSalvo', this.produtos)
                this.limparCampos()
                //console.log(this.produtos) 
            },
            limparCampos(){
                this.produtos.nome = ""
                this.produtos.valor = ""
                this.produtos.qtdade = ""
            }
        
    }
}

</script>

<style>


</style>