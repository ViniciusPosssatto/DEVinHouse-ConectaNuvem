<template>
  <div>
    <Relogio :listaVoltas="listadeVoltas"/>
      <div v-show="listadeVoltas.length > 0" id="listaVoltas">
            <ul v-for="(item, key) in listadeVoltas" :key="key">
              <li>{{key + 1}} + {{item}}</li>
            </ul>
        </div>
        <button  @click.prevent="$emit('addlista', [hora, minuto, segundos])">Marcar Volta</button>
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
      hora: String,
      minuto: String,
      segundos: String,
      milisegundos: String,
      listadeVoltas: {
       type: Array
     }  
    },
    methods: {
    
    }
            
}


</script>

<style>

</style>