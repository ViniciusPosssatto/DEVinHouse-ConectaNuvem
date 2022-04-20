<template>
  <div>
    <div>
      <h1>A cor deve ser {{ cor }}!</h1>
    </div>
    <div>
     
     <!--   {{ verificaIdade }}
      
     outro modo
      <p v-show= "verificaIdade">
        {{ idade }}
      </p>
      
      -->
    </div>
    <CorVermelha @ApareceVermelho="corVermelho"/>
    <!-- 
          O componente Pai vai chamar um evento do filho através do @.
         Nesse caso o evento é o click através do $emit.
         No momento que o o click for realizado, o componente filho vai emitir o aviso 
         e o método corVermelho vai ser executado.
         Neste caso o método irá atribuir o valor "vermelho" ao parâmetro "cor" que está instanciado na tela no h1.
    --> 

    <CorAzul @ApareceAzul="mudacorAzull"/>
    <!-- 
      Outro modo é definir a cor no componente filho e passar ela por parâmetro na hora que 
      vai chamar o $emit e aqui no componente pai, passar a "cor" (nesse caso) como parâmetro da 
      função/método que vai atribuir o valor à variável "cor".
    --> 
    <CorVerde @ApareceVerde="corVerdee"/>

  </div>
</template>

<script>
import CorVermelha from "./components/CorVermelha.vue";
import CorAzul from "./components/CorAzul.vue";
import CorVerde from "./components/CorVerde.vue";


export default {
  name: 'App',
  data() {
    return {
      cor: '',
      //idade: 18
    }
  },
  computed: {
    //verificaIdade() {
      //return idade >= 18 ? 'É maior de idade' : 'É menor de idade';
      //outro jeito
      // return idade >= 18 ? true : false;
    ///}
  },
  watch: { //ulitizado para acompanhar os valores que a variável recebe ao longo dos eventos
    cor(novoValor, valorAntigo){
      console.log('novo valor: ' + novoValor)
      console.log('antigo: ' + valorAntigo)
    }
  },
  components: {
    CorVermelha,
    CorAzul,
    CorVerde
  },
  methods: {
    corVermelho(){
      this.cor = 'vermelho'
    },
    corVerdee(){  
      this.cor = 'verde'
    },
    mudacorAzull(cor){
      this.cor = cor   // cor é o parâmetro passado pelo evento click do comp filho
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
