<template>
  <div class="exibir-texto">
      <h2>Receber texto</h2>
      <p> Meu nome é {{ nomes }}</p>
  </div>
</template>

<script>
export default {
    props: {
        nomes: {

        }
    },
    data(){
        return{
            nome: null
        }
    }

}
</script>

<style>

</style>