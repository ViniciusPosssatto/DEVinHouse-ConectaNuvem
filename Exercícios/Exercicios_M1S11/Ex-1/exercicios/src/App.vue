<template>
  <div class="app">
    <div class="row">
      <div class="col-3">
          <label for="senha">CEP</label>
          <input type="number" class="form-control" v-model="cep">
      </div>
      <div class="col-12 mt-2">
          <button @click="buscaCep" class="btn btn-primary">Buscar</button>
      </div>
    </div>
    <p v-show="vcep">Você mora na {{ rua }}, da cidade de {{ cidade }} / {{ estado }} e o seu DDD é {{ ddd }}.</p>
    <h3>Dados de Endereço</h3>
          <br>
          <div class="row g-3">
            <div class="col-4">
              <label>CEP</label>
              <input type="number" name="cep" class="form-control" v-model="user.cep">
            </div>
            <div class="col-4">
              <label>Cidade</label>
              <input type="text" name="cidade" class="form-control" v-model="user.cidade">
            </div>
            <div class="col-4">
              <label>Estado</label>
              <input type="text" name="estado" class="form-control" v-model="user.estado">
            </div>
            <div class="col-4">
              <label>Logradouro</label>
              <input type="text" name="logradouro" class="form-control" v-model="user.logradouro">
            </div>
           
            <div class="col-7">
              <label>Complemento</label>
              <input type="text" name="complemento" class="form-control" v-model="user.complemento">
            </div>
            <div class="col-5">
              <label>Bairro</label>
              <input type="text" name="bairro" class="form-control" v-model="user.bairro">
            </div>
            <div class="col-12 mt-2">
          <button @click="buscaCep" class="btn btn-primary">Buscar</button>
      </div>  
          </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data(){
    return{
      user: {
        cep: '',
        rua: '',
        estado: '',
        cidade: '',
        ddd: '',
        vcep: false

      }
    }
  },
  methods: {
   buscaCep() {
       axios.get(`https://viacep.com.br/ws/${this.user.cep}/json`)
        .then((response) => {
          //console.log(response)
          this.user.cidade = response.data.localidade;
          this.user.estado = response.data.uf;
          this.user.logradouro = response.data.logradouro;
          this.user.complemento = response.data.complemento;
          this.user.bairro = response.data.bairro;
        }) .catch ((error) => {
          console.log(error.message)
   
      })
   }
  }
}
</script>

<style>

</style>
