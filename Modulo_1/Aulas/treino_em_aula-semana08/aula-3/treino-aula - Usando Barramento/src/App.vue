<template>
  <div id="app">
    <EmitirTexto />
    <ExibirTexto />
  </div>
</template>

<script>
import EmitirTexto from "./components/EmitirTexto.vue";
import ExibirTexto from "./components/ExibirTexto.vue";



export default {
  name: 'App',
  components: {
    EmitirTexto,
    ExibirTexto
  },
  data(){
    return {
      textoRecebido: null
    }
  },
  methods: {
    receberTexto(texto) {
      console.log(texto)
      this.textoRecebido = texto;
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
