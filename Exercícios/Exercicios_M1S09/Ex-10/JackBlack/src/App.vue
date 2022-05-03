<template>
  <div class="app">
    <div class="container">
      <div class="col-md-12">
        <h1>Jack Black</h1>
        <button type="button" class="btn btn-primary" @click="novoJogo">Novo Jogo</button>
        <h4 v-html="rodada"></h4>

        <hr/>

        <h5 v-text="adversario"></h5>
        <h5>Jogador: {{ total }} pontos</h5>
        <h5>Jogadas restantes: {{ jogadas }}</h5>
        <hr/>

        <h3>Carta: {{ carta }}</h3>
        <button @click="novaCarta" class="btn btn-success">Nova Carta</button>
        <button @click="pararJogo" class="btn btn-info">Parar</button>
      </div>
    </div>

  </div>
</template>

<script>


export default {
  name: 'App',
  data(){
    return{
      carta: '',
      adversario: `Adversário: 17 pontos`,
      rodada: "<h4 class='jogando'>Você está jogando!</h4>",
      jogadas: 5,
      total: 0
    }
  },
  methods: {
    novaCarta(){
      this.carta = Math.floor(Math.random() * 11 + 1)
      this.total += this.carta
      this.jogadas--
      if(this.jogadas >= 0 && this.total > 21){
        return this.rodada = "<h4 class='perdeu'>Você perdeu!</h4>"
      } else if(this.jogadas < 0 && this.total < 17){
        return this.rodada = "<h4 class='perdeu'>Você perdeu!</h4>"
      } else if(this.total === 21){
        return this.rodada = "<h4 class='ganhou'>Você GANHOU!!</h4>"
      } else if(this.jogadas <= 0 && this.total < 17){
        return this.rodada = "<h4 class='perdeu'>Você perdeu!</h4>"
      } else if(this.jogadas <=0 && this.total > 17 && this.total <= 21){
        return this.rodada = "<h4 class='ganhou'>Você GANHOU!!</h4>"
      } else if(this.jogadas <=0 && this.total === 17){
        return this.rodada = "<h4 class='empatou'>Empatou!</h4>"
        }
    },
    novoJogo(){
      this.carta = ''
      this.total = 0
      this. rodada = "<h4 class='jogando'>Você está jogando!</h4>",
      this.jogadas = 5
    },
    pararJogo(){
      if(this.total >= 18 && this.total <= 21){
        return this.rodada = "<h4 class='ganhou'>Você GANHOU!!</h4>"
      } else if(this.total === 17){
        return this.rodada = "<h4 class='empatou'>Empatou!</h4>"
      } else{
        return this.rodada = "<h4 class='perdeu'>Você perdeu!</h4>"
      }
    }
  }
}
</script>

<style>
body{
  margin-top: 30px;
  background-color: rgb(146, 144, 144);
}
.container{
  border: 3px solid black;
  border-radius: 20px;
  width: 500px;
  padding: 15px;
  background-color: rgb(255, 255, 255);
}
h1{
  color: blue;
}
button{
  margin: 10px 10px 5px 0;
  width: 140px;
}
.jogando{
  background-color: rgb(22, 110, 241);
  padding: 8px;
  width: 250px;
  color: aliceblue;
  border-radius: 20px;
  text-align: center;
}
.ganhou{
  background-color: rgb(7, 161, 46);
  padding: 8px;
  width: 200px;
  color: aliceblue;
  border-radius: 20px;
  text-align: center;
}
.perdeu{
  background-color: rgb(243, 38, 2);
  padding: 8px;
  width: 180px;
  color: aliceblue;
  border-radius: 20px;
  text-align: center;
}
.empatou{
  background-color: rgb(227, 243, 8);
  padding: 8px;
  width: 250px;
  color: rgb(0, 0, 0);
  border-radius: 20px;
  text-align: center;
}
hr{
  width: 100%;
  color: black;
  height: 1px;
  background-color:black;
}
</style>
