<template>
    <div class="form-produtos">
      <Form>
          <div>
              <div>
                <label for="nome-produto">Insira seu produto aqui:</label>
                <Field id="nome-produto" name="nome" type="text" v-model="produto.nome" :rules="validations.validaNome"/>
                    <div class="error">
                        <span>
                            <ErrorMessage name="nome"/>
                        </span>
                    </div>
                    
              </div>
              <div>
                <label for="valor-produto">Insira o valor dele aqui:</label>
                <Field id="valor-produto" name="valor" type="number" v-model="produto.valor" :rules="validations.validaValor"/>
                <div class="error">
                        <span>
                            <ErrorMessage name="valor"/>
                        </span>
                    </div>
              </div>
                <button id="btn-add" type="button" @click="addProduto" :disabled="habilitaBtn">Adicionar</button>
          </div>
      </Form>

    </div>
</template>

<script>
import {Form, Field, ErrorMessage } from 'vee-validate'
import Validations from '@/validations'
export default {
    name: 'FormProduto',
    data() {
        return {
            produto: {
                nome: null,
                valor: null
            },
            habilitaBtn: false,
            validations: null
        }
    },
    components: {
        Form,
        Field,
        ErrorMessage,
        
    },
    methods: {
        addProduto() {
            console.log(this.produto)
        },
        beforeMount(){
            this.validations = Validations
        }

        // SUBSTITUIDO ISSO PELO ARQUIVO VALIDATIONS -------
    //     validaNome(atributo) {
    //     if(!atributo){
    //         this.habilitaBtn = true;
    //         return 'O campo nome é obrigatório!'
    //     }
    //     this.habilitaBtn = false
    //     return true
    // },
    // validaValor(atributo) {
    //     if(atributo <= 0){
    //         this.habilitaBtn = true
    //         return 'O campo valor tem que ser maior que zero!'
    //     }
    //     this.habilitaBtn = false
    //     return true
    // }
}
    
    
    

}
</script>

<style>

</style>