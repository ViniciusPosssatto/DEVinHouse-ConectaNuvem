<template>
    <div id="cronometro">
        <h2>Relógio</h2>

        <p>{{ hora }}:{{ minuto }}:{{ segundos }}</p>

        <MarcadorV :listadeVoltas="listaVoltas"/>
        
    </div>
</template>

<script>

import MarcadorV from "./MarcadorV.vue"

export default {
    name: 'RelogioC',
    components: {
        MarcadorV,
    
    },
    props: {
        hora: String,
        minuto: String,
        segundos: String,
        listaVoltas: []
    }
}
</script>

<style>

</style>