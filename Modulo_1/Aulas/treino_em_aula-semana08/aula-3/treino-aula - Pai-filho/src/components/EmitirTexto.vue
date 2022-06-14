<template>
  <div class="emitir-texto">
      <h2>Emissor</h2>
      <label for="">Insira seu nome:</label>
      <input type="text" v-model="nome"/>
      <button type="button" @click="$emit('emitirTexto', nome)">Emitir</button>
  </div>
</template>

<script>
export default {
    data(){
        return {
            nome: null
        }
    }
}
</script>

<style>

</style>