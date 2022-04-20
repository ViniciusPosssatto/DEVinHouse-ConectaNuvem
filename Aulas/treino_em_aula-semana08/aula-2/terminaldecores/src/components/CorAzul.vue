<template>
  <div>
      <button type="button" @click="$emit('apareceAzul', cor)">Azul</button>
    <!-- 
      atribui a variável cor no data() e passa ela como parâmetro no evento de click
      @click="$emit('nome do evento a chamar no pai', parâmetro a enviar)".
    --> 
  </div>
</template>

<script>
export default {
    name: "CorAzul",
    data() {
        return {
            cor: 'azul'
        }
    }
    
}
</script>

<style>

</style>