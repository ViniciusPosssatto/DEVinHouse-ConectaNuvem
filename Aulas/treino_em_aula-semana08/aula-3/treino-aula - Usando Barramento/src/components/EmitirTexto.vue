<template>
  <div class="emitir-texto">
      <h2>Emissor</h2>
      <label for="">Insira seu nome:</label>
      <input type="text" v-model="nome"/>
      <button type="button" @click="emitirTexto">Emitir</button>
  </div>
</template>

<script>
import barramento from '@/barramento'
export default {
    data(){
        return {
            nome: null
        }
    },
    methods: {
        emitirTexto() {
            barramento.$emit('textoEmitido', this.nome)
        }
    }
}
</script>

<style>

</style>