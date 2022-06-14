<template>
  <div>
      <button type="button" @click="$emit('apareceVermelho')">Vermelho</button>
      <!-- 
          o componente filho vai emitir um evento de click quando o componente pai requisitar.
          No componente pai está @apareceVermelho, que é o parâmetro do evento passado pra ele. 
          O @ seria o bind/$emit entre eles, o evento.
      --> 
  </div>
</template>

<script>
export default {
    name: "CorVermelha",
    
}
</script>

<style>

</style>