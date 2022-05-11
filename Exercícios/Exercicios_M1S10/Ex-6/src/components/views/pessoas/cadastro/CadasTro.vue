<template>
  <div class="cadastro">
    <h1>Cadastro!</h1>
    <form @submit.prevent="addPessoa" >
      <div class="row">
        <div class="col-4">
          <label for="nome">Digite seu nome:</label>
          <input type="text" id="nome" v-model="pessoa.nome">
          
        </div>
        <div class="col-4">
          <label for="idade">Data de nascimento</label>
          <input type="date" id="idade" v-model="pessoa.nascimento">
          
        </div>
        <div class="col-4">
          <button type="submit" class="btn btn-sm btn-primary">Adiciona Pessoa</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>

export default {
  
  name: 'App',
  data(){
    return{
      pessoa: {
        id: new Date().getTime(),
        nome: '',
        nascimento: ''
      },
      show: true
     
    }
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