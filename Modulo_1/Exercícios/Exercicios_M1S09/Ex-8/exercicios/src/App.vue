<template>
  <div id="app" class="container">
    <div>
      <form>
        <label for="nome">Digite seu nome:</label>
          <input type="text" name="nome" id="nome" v-model="pessoa.nome">
          <label for="idade">Digite sua idade:</label>
          <input type="number" name="idade" id="idade" v-model="pessoa.idade">
          <button type="button" @click="salvaPessoa()" class="btn-primary">Salvar</button>
      </form>
    </div>
    <hr>
    <div class="text-center" v-if="pessoas.length === 0">
      Não há pessoas cadastradas
    </div>
    <div v-else>
      <table class="table">
        <tr>
          <th>Id</th>
          <th>Nome</th>
          <th>Idade</th>
        </tr>
        <tr v-for="(pessoa, index) in pessoas" :key="index"> 
          <td>{{ index + 1}}</td>
          <td>{{ pessoa.nome }}</td>
          <td>{{ pessoa.idade }}</td>
        </tr>
      </table>
      <div>
        <button @click="limpar()">Limpar Lista</button>
      </div>
    </div>
    
   
  </div>
</template>

<script>

export default {
    name: "app",
    data() {
        return {
          pessoa:{
            nome: '',
            idade: ''
          },
           pessoas:[]
        };
    },
    methods: {
      salvaPessoa(){
        this.pessoas.push({
          "nome": this.pessoa.nome,
          "idade": this.pessoa.idade
        })
        this.pessoa.nome = ""
        this.pessoa.idade = ""
      },
      limpar(){
        this.pessoas = []
      }
    },
    
}
</script>

<style>
body{
  margin-top: 40px;
}
</style>
