<template>
  <div class="cadastro">
    <h1>Cadastro!</h1>
    <vee-form @submit="addPessoa" :validation-schema="schema" v-slot="{ errors }">
      <div class="row">
        <div class="col-4">
          <label for="nome">Digite seu nome:</label>
          <vee-field name="nome" type="text" id="nome" v-model="pessoa.nome"/>
          <span class="text-danger" v-text="errors.nome" v-show="errors.nome"></span>
          
        </div>
        <div class="col-4">
          <label for="nascimento">Data de nascimento</label>
          <vee-field name="nascimento" type="date" id="nascimento" v-model="pessoa.nascimento"/>
          <span class="text-danger" v-text="errors.nascimento" v-show="errors.nascimento"></span>

        </div>
        <div class="col-4">
          <button type="submit" class="btn btn-sm btn-primary">Adiciona Pessoa</button>
        </div>
      </div>
    </vee-form>
  </div>
</template>

<script>
import { Form, Field, defineRule } from 'vee-validate';


defineRule("required", value => {
  if(!value || value.length === 0) {
    return "Campo obrigatório!"
  }
  return true;
});

defineRule("data", value => {
  if (new Date(value) > new Date()){
    return "A data deve ser anterior a data atual!"
  }
    return true;
});


export default {
  name: 'App',
  data(){
    return{
      pessoa: {
        id: Date.now(),
        nome: '',
        nascimento: ''
      },
      schema: {
        nome: "required",
        nascimento: "required|data"
      }
    }
  },
  components: {
    'vee-form': Form,
    'vee-field': Field
  },
  methods: {
    
    addPessoa(){
    //console.log(this.pessoa)
    this.$store.commit('addCadastro', this.pessoa)
    this.pessoa = {}
    },
   
  }
}
</script>

<style>
body{
  padding: 0 50px;
}
input{
  margin-left: 10px;
}
.aviso{
  color: red;
  font-size: 25px;
  margin-top: 50px;
}
p{
  font-size: 15px;
  color: black;
}
</style>