<template>
  <div>
    <div id="buttons">
      <button @click.prevent="relogio">Iniciar</button>
      <button @click.prevent="parar">Parar</button>
      <button @click.prevent="zerar">Zerar</button>
    </div>

    <Relogio @addlista="marcarVolta" :listaVoltas="listadeVoltas" :hora="hora < 10 ? '0'+hora : hora" :minuto="minuto < 10 ? '0'+minuto : minuto" :segundos="segundos < 10 ? '0'+segundos : segundos"/>
    <MarcadorV :listadeVoltas="listaVoltas"/>
</div>
  
</template>

<script>

import Relogio from "./components/Relogio.vue"

export default {
  name: 'App',
  components: {
    Relogio
  },
  data(){
    return{
      hora: 0,
      minuto: 0,
      segundos: 0,
      contador: 0,
      listadeVoltas: []
    }
  },
  methods: {
    addZero(tempo){
      return tempo < 10 ? "0"+tempo : tempo
    },
    
    zerar(){
      this.hora = 0
      this.minuto = 0
      this.segundos = 0
    },
    parar(){
      clearInterval(this.contador)
    },
    marcarVolta(tempo){
      
      var volta = `${this.addZero(tempo[0])}:${this.addZero(tempo[1])}:${this.addZero(tempo[2])}`
      this.listadeVoltas.push(volta)
      console.log(this.listadeVoltas)
      },
    relogio(){
      
      this.contador = setInterval(() => {
        this.segundos++
        if(this.segundos == 60){
          this.minuto++
          this.segundos = 0
        }
        if(this.minuto == 60){
          this.hora++
          this.minuto
        }
        if(this.hora == 60){
          this.minuto = 0
          this.hora = 0
          this.segundos = 0
        }
  
      console.log(this.segundos)
      }, 1000)
      
    }
  }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
