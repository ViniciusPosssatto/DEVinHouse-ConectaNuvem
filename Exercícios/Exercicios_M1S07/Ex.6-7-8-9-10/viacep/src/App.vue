<template>
  <div>
    <FormularioPessoa/>
  </div>
</template>

<script>
import FormularioPessoa from './components/FormularioPessoa.vue'


export default {
  name: 'App',
  components: {
    FormularioPessoa
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
