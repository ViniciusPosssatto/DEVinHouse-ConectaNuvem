<template>
  <div class="app-principal">
    <div class="painel">
        <div class="botao-ini">
          <button type="button" class="btn btn-primary posicao total painel" data-bs-toggle="modal" data-bs-target="#exampleModal">
            Adicionar item
          </button>
          <h3 class="posicao">Lista de compras</h3>
        </div>
    </div>
    
    <ComponenteModal @produtoSalvo="adicionaProduto" />
    <PrimeiroComponente :listas="listas" @limparLista="limparListas"/>

    <button class="btn btn-danger total painel posicao" @click="limparListas" v-if="listas.length > 0">Limpar Lista</button>
    
    <div class="rodape">
      <div class="painel">
        <div class="total">
          <p class="valor-tt">O total gasto é : R$ {{ total }}</p>
        </div>
      </div>
    </div>

  </div>

</template>

<script>
  import ComponenteModal from './components/ComponenteModal.vue'
  import PrimeiroComponente from './components/primeiroComponente.vue'

  export default {
    name: 'App',
    data(){
      return {
        listas: [],
        total: 0
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
          "valor": event.valor,
          "valida": false
          })
          this.calcularTotal()
      },
      limparListas(event){
        this.listas.splice(event);
      },
      calcularTotal() {                   // soma o valor dos itens vezes suas quantidades
        this.listas.forEach( item => {
          if(item.valida == false){
            this.total += Number(item.valor * item.qtdade)
            item.valida = true    //add uma verificação para ver se ele já foi contabilizado
          }
          //console.log(item)
        })
      }
      
    }
  }
</script>

<style>
 .total{
    margin-left: auto;
    margin-right: auto;
 }
 .painel{
    display: flex;
    align-content: center;
    align-items: center;
 }
 .rodape{
   position: absolute;
   bottom: 0;
   width: 100%;
   height: 60px;
   background-color: rgb(115, 115, 116);
   color: #000000;
 }
 .botao-ini{
    margin-left: auto;
    margin-right: auto;
 }
  .posicao{
    margin-top: 15px;
  }
  .valor-tt{
    font-size: 20px;
    margin-top: 5px;
  }
</style>