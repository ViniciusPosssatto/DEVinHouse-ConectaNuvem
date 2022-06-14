<template>
<div class="container">
  <div>
    <h1>Marcador de voltas</h1>
  </div>
    
    <div id="btn">
      <button class="btn btn-primary" @click.prevent="relogio()">Iniciar</button>
      <button class="btn btn-success" @click.prevent="parar()">Parar</button>
      <button class="btn btn-warning" @click.prevent="zerar()">Zerar</button>
    </div>

    <TemporizadorC 
    @parar="parar" 
    @limpatempo="limpatempo" 
    @addlista="marcarVolta" 
    :listaVoltas="listadeVoltas" 
    :hora="addZero(hora)" 
    :minuto="addZero(minuto)" 
    :segundos="addZero(segundos)" 
    :milisegundos="addZero(milisegundos)"
    />
   
</div>
</template>

<script>
import TemporizadorC from "./components/TemporizadorC.vue"
export default {
  name: 'App',
  components: {
    TemporizadorC
  },
  data(){
    return{
      hora: 0,
      minuto: 0,
      segundos: 0,
      milisegundos: 0,
      contador: 0,
      listadeVoltas: [],
    
    }
  },
 
  methods: {
    limpatempo(){
      this.listadeVoltas = []
    },
    addZero(tempo){
      return tempo < 10 ? "0"+Number(tempo) : `${tempo}`
    },
    marcarVolta(tempo){
      var volta = `${this.addZero(tempo[0])}:${this.addZero(tempo[1])}:${this.addZero(tempo[2])}:${this.addZero(tempo[3])}`
      this.listadeVoltas.push(volta)
    },
    zerar(){
      this.hora = 0
      this.minuto = 0
      this.segundos = 0
      this.milisegundos = 0
    },
    parar(){
      clearInterval(this.contador)
    },
    relogio(){
      this.contador = setInterval(() => {
        this.milisegundos++
        if(this.milisegundos == 100){
          this.segundos++
          this.milisegundos = 0
        }
        
        if(this.segundos == 60){
          this.minuto++
          this.segundos = 0
        }
        
        if(this.minuto == 60){
          this.hora++
          this.minuto = 0
        }
        if(this.hora == 60){
          this.minuto = 0
          this.hora = 0
          this.segundos = 0
        }
        
        console.log(this.segundos)
      }, 10)
    }
  }
}
</script>

<style>
body{
  background-color: black;
  color: rgb(223, 201, 8);

}
button{
  width: 100px;
  margin: 20px 0 10px 15px;
  display: flex;
}
.btn-info{
  width: 130px;
}
.container {
  width: 500px;
  height: 500px;
  display: block;
  justify-content: center;
  align-items: center;
  gap: 35px;
}
h1{
  margin-left: 20px;
}
</style>