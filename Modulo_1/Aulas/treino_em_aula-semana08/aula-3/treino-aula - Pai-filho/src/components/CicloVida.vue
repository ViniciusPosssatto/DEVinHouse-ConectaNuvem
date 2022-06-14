<template>
  <div class="ciclo-vida">
      <h1>Ciclo de vida de um componente vue</h1>
      <div class="nomes" v-for="nome in nomes" :key="nome">
          <p>{{ nome }}</p>

      </div>
  </div>
</template>

<script>
export default {
    data(){
        return {
            nomes: ''
        }
    },
    beforeCreate(){
        console.log('Antes de ser Criado')
    },
    created(){
        console.log('Criado')
    },
    beforeMount(){
        console.log('Antes de ser montado')
        this.nomes = ['Kauã', 'Julia', 'Maycon']
    },
    mounted() {
        console.log('Montado')
    },
    beforeUpdate(){
        console.log('Está sendo preparado para atualizar')
    },
    updated(){
        console.log('Componente atualizado')
    },
    beforeDestroy(){
        console.log('Eu vou cair')
    },
    destroyed(){
        console.log('caiu')
    }

}
</script>

<style>

</style>