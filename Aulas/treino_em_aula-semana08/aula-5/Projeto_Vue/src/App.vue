<template>
  <div class="app-principal">

    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
      Adicionar item
    </button>
    <ComponenteModal @movimentacaoSalva="adicionaMovimentacao"/>
    <primeiroComponente :movimentacoes="movimentacoes" @excluirMovimentacao="excluirMovimentacao"/>

    <p>{{ movimentacao }}</p>
  <div class="rodape">
    <div class="container">
      <div class="total-entradas">
        <p>R$ {{ totalEntradas }}</p>
      </div>
      <div class="total-saidas">
        <p>R$ {{ totalSaidas }}</p>
      </div>
      <div class="saldo">
        <p>R$ {{ saldo }}</p>
      </div>
    </div>
  </div>
   

  </div>

</template>

<script>
  import ComponenteModal from './components/ComponenteModal.vue'
  import primeiroComponente from "./components/primeiroComponente.vue"

  export default {
    name: 'App',
    data(){
      return {
        movimentacoes: [],
        totalEntradas: 0,
        totalSaidas: 0,
        saldo: 0
      }
    },
    components: {
      primeiroComponente,
      ComponenteModal
     
    },
    methods: {
      adicionaMovimentacao(event){
        this.movimentacoes.push({
          "nome": event.nome,
          "valor": event.valor,
          "info": event.info,
          "data": event.data,
          "tipo": event.tipo
        })
        console.log(this.movimentacoes)
      },
      excluirMovimentacao(indice) {
        this.movimentacoes.splice(indice, 1);
      }

    }
  }
</script>

<style>
 
</style>