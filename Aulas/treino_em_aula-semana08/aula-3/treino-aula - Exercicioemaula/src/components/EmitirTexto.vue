<template>
  <div class="emitir-texto">
    <h1>
        Digite sua idade:
    </h1>
    <input type="number" v-model="idade">
    <button @click="emitirValor">Testar</button>
  </div>
</template>

<script>
import barramento from "@/barramento"
export default {
    data(){
        return {
            idade: null,
            maiorIdade: false
        }
    },
    methods: {
        emitirValor(){
            barramento.$emit('idadeEmitida', this.idade)
        }
    }
   
}
</script>

<style>

</style>