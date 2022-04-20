<template>
<primeiroComponente/>
<p>{{ produto }}</p>

</template>

<script>
  import primeiroComponente from "./components/primeiroComponente.vue"

  export default {
    name: 'App',
    data(){
      return {
        produto: null
      }
    },
    components: {
      primeiroComponente
     
    },
  }
</script>

<style>
 
</style>