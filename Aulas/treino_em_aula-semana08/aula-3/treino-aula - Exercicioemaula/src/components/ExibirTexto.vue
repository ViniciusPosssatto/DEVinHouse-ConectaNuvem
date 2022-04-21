<template>
  <div class="exibir-texto">
      <p>{{ maiorIdade }}</p>
      <p>{{ verificaMaiorIdade }}</p>
  </div>
</template>

<script>
import barramento from '@/barramento'

export default {
    data(){
        return{
            idade: null,
            maiorIdade: null
        }
    },
    created(){
        barramento.$on('idadeEmitida', idade => {
            this.idade = idade
            if(this.idade >= 18){
              this.maiorIdade = `Você é maior de idade`
            }else{
              this.maiorIdade = `Você é menor de idade`
            }
        })
        
    },
    computed: {
        verificaMaiorIdade() {
            barramento.$on('idadeEmitida', idade => {
                this.idade = idade;
            })
            return this.idade >= 18 ? 'É maior idade' : 'É menor idade'
        }
    }
}
</script>

<style>

</style>