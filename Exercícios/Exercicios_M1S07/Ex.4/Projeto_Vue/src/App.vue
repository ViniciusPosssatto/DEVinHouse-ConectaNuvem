<template>
  <h1>Olá, mundo!</h1>
  <primeiroComponente/>
  <p>Meu nome é {{ nome }} e trabalho com {{ prof }}.</p>
  <segundoComponente/>
</template>

<script>
  import primeiroComponente from "./components/primeiroComponente.vue"
  import segundoComponente from "./components/segundoComponente.vue"
  export default {
    name: 'App',
    data(){
      return {
        nome: "qlq um kk",  // primeiro a ser executado, logo em seguida vem os hooks
        prof: "programação"
      }
    },
    components: {
      primeiroComponente,
      segundoComponente
    },
    created() {           //hook para modificação
      setTimeout(() => {  //add um tempo para execução dele
        this.nome = "Agora com tempo"
      }, 2000);  //vai ser apresentado 2s depois da primeira execução
      
    },
    mounted() {                   //hook para modificação
      setTimeout(() => {            //add um tempo para execução dele
        this.nome = "Outra com mais hierarquia"
      }, 5000);  //irá ser o último a ser apresentado e vai continuar na tela
      
    }
  }
</script>

<style>
  h1{
    color: blue;
  }
  h2{
    color: red;
  }
  p{
    font-family: 'Courier New', Courier, monospace;
    font-size: 20px;
  }
</style>