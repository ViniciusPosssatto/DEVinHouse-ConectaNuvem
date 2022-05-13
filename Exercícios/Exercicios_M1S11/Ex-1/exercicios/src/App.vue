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
    
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data(){
    return{
      cep: '',
      rua: '',
      estado: '',
      cidade: '',
      ddd: '',
      vcep: false
    }
  },
  methods: {
    buscaCep(){
      axios.get(`https://viacep.com.br/ws/${this.cep}/json`)
        .then((response) => {
          //console.log(response)
          this.rua = response.data.logradouro;
          this.estado = response.data.uf;
          this.cidade = response.data.localidade;
          this.ddd = response.data.ddd;
          this.vcep = true
          this. cep = ''
        }) .catch ((error) => {
          console.log(error.message)
        })
    }
  }
}
</script>

<style>

</style>
