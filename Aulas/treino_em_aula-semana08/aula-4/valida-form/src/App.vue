<template>
  <div class="validacao">
    <FormProduto />
  </div>
</template>

<script>
import FormProduto from "./components/FormProduto.vue";



export default {
    components: { 
      FormProduto 
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
