<template>

    <div>
        <hr>
        <div>
            <button class="btn btn-info" @click="$emit('addlista', [hora, minuto, segundos, milisegundos])">Marcar Volta</button>
            <button class="btn btn-danger" @click="$emit('limpatempo')">Limpar</button>
        </div>

        <h1 @dblclick="$emit('parar')">{{ hora }}:{{ minuto }}:{{ segundos }}:{{ milisegundos }}</h1>

        <Transition name="bounce">
            <div v-if="listaVoltas.length > 0" id="listaVoltas">
                <ul v-for="(item, key) in listaVoltas" :key="key">
                  <li> {{key + 1}} - {{item}}</li>
                </ul>
            </div>
        </Transition>
            
    </div>
</template>

<script>
export default {
    name: "TemporizadorC",
    props: {
        hora: String,
        minuto: String,
        segundos: String,
        milisegundos: String,
        listaVoltas: {}
    }
}
</script>

<style>
hr{
    color: white;
    width: 370px;
}
li{
    font-size: 20px;
    color: rgb(8, 248, 0);
    margin-left: 40px;
}
</style>