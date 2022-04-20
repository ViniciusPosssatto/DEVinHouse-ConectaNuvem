<template>
  <div>
    <Relogio :listaVoltas="listadeVoltas"/>
      <div v-show="listadeVoltas.length > 0" id="listaVoltas">
            <ul v-for="(item, key) in listadeVoltas" :key="key">
              <li>{{key - item}}</li>
            </ul>
        </div>
        <button  @click="$emit('addlista', [hora, minuto, segundos])">Marcar Volta</button>
  </div>
</template>

<script>
import Relogio from "./Relogio.vue"


export default {
    name: 'MarcadorV',
    components: {
    Relogio,
    },
    props: {
     listadeVoltas: []   
    },
    methods: {
    
    }
            
}


</script>

<style>

</style>