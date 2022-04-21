<template>
  <div class="exibir-texto">
      <h2>Receber texto</h2>
      <p> Meu nome é {{ nome }}</p>
  </div>
</template>

<script>
import barramento from '@/barramento'
export default {
    data(){
        return{
            nome: null
        }
    },
    created(){
        barramento.$on('textoEmitido', texto => {
            this.nome = texto
        })
    }

}
</script>

<style>

</style>