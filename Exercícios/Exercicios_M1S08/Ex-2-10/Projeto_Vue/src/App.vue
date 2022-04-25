<template>
  <div class="app-principal">

    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
      Adicionar item
    </button>

    <primeiroComponente />

    <p>{{ produto }}</p>

    <ComponenteModal id="exampleModal"/>

  </div>

</template>

<script>
  import ComponenteModal from './components/ComponenteModal.vue'
  import primeiroComponente from "./components/primeiroComponente.vue"

  export default {
    name: 'App',
    data(){
      return {
        produto: null
      }
    },
    components: {
      primeiroComponente,
      ComponenteModal
     
    },
    methods: {

    }
  }
</script>

<style>
 
</style>