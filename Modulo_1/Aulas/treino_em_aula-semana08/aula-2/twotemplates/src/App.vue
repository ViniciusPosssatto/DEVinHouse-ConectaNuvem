<template>
  <div>
    <h2>Contador de inscritos</h2>
    <label>Quantidade de vagas:</label>
    <input type="number" v-model="qtdVagas">
     <contador-inscritos :vagas="qtdVagas" @encerrarVagas="vagasEncerrar"/>
  {{ numInsc }}
  </div>
 
</template>

<script>
import ContadorInscritos from './components/ContadorInscritos.vue'


export default {
  name: 'App',
  components: {
    ContadorInscritos
  },
  data() {
    return {
      qtdVagas: '',
      numInsc: ''
    }
  },
  methods: {
    vagasEncerrar(){
      alert()
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
