<template>
  <div class="div-pai">
    <label >CEP</label>
    <input type="number" v-model="cepp" placeholder="Apenas números">
    <input type="button" value="Buscar" @click="buscar">
    {{ cepp }}
  </div>
</template>

<script>
import FormularioPessoa from "./FormularioPessoa.vue";
export default {
  name: 'ViaCep',
  components:{
    FormularioPessoa
  },

  data() {
    return{
      cepp: "",
      localidade: null,
      uf: null
      
    }
  },
  methods: {
    buscar(){
      try {
        const cep = this.cepp;
        const url = `https://viacep.com.br/ws/${cep}/json`;
        
          const resposta = fetch(url);
          console.log(resposta);
          const conteudo = resposta.json();
          console.log(conteudo);
       
    
        this.localidade = conteudo.localidade;

      } catch (erro) {
        console.log('deu ruim')
      }
    },
    // buscar() {
    //   this.buscarCEP(cep)
    // }
  }
}
</script>

<style>

</style>