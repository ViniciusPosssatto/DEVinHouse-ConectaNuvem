<template>
  <div>
      <h3>Porcentagem de vagas preenchidas:</h3>
      {{ calcPorcentagem }} %
      
      <div class="botoes">
          
      <button type="button" @click="numInsc++">Adiciona inscrito</button> 
      <button type="button" @click="numInsc--">Retira inscrito</button>
      
      </div>
      <p>Quantidade de pessoas inscritas: {{ numInsc }}</p>
        {{ vagas }}
  </div>
</template>

<script> 
export default {
    data(){
        return {
            numInsc: 0
        }
    },
    watch: {
        qtdInsc(novoValor) {
           if(novoValor == this.qtdInsc){
               this.encerrarVagas()
           }
        }
    },
    props: {
        vagas:{
            type: Number,
            require: true
        },
    },
    computed: {
        calcPorcentagem() {
            return ((this.numInsc * 100) / this.vagas).toFixed(2)
            
        
        },
    },
    methods: {
        encerrarVagas() {
            this.$emit('Vagas encerradas!')
        }
    }
    
}
</script>

<style>

</style>