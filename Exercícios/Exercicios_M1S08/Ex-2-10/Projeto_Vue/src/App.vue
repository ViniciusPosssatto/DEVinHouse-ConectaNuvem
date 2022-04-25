<template>
  <div class="app-principal">
    <h3>Lista de compras</h3>
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
      Adicionar item
    </button>
    <ComponenteModal @produtoSalvo="adicionaProduto" />
    <PrimeiroComponente :listas="listas" @limparLista="limparListas"/>


    
  <button class="limpar-lista" @click="limparListas">Limpar Lista</button>
  </div>

</template>

<script>
  import ComponenteModal from './components/ComponenteModal.vue'
  import PrimeiroComponente from './components/primeiroComponente.vue'

  export default {
    name: 'App',
    data(){
      return {
        listas: []
      }
    },
    components: {
      ComponenteModal,
      PrimeiroComponente
    },
    methods: {
      adicionaProduto(event){
        this.listas.push({
          "nome": event.nome,
          "qtdade": event.qtdade,
          "valor": event.valor
          })
      },
      limparListas(event){
        this.listas.splice(event);
      }
    }
  }
</script>

<style>
 .limpar-lista{
   position: absolute;
   bottom: 0;
   display: flex;
   align-content: center;
   align-items: center;
   
 }
</style>