<template>
  <div class="app">
    <transition name="header" mode="in-out">  <!-- o mode é o método de selecionar a forma de transição in-out (vem e vai) e out-in (vai e vem) -->
      <!-- Aqui vai alterar o h1 para aparecer ou não quando clica no botão
          - pra sumir ele vai negar a própria variável deixando ela false
      -->
        <h1 v-show="show">Header!</h1>
    </transition>
     
    <button @click="alterar">Alterar Campo</button>
  </div>
</template>

<script>


export default {
  name: 'App',
  data(){
    return{
      show: true
    }
  },
  methods: {
    alterar(){
      return !this.show
    }
  }
}
</script>

<style>

/*Primeiro estilo*/
.header-leave-to,
.header-enter-from{
  /*background-color: white;*/
  opacity: 0;
  font-size: 0px
}

/*Segundo estilo*/
.header-leave-from,
.header-enter-to{
  /*background-color: black;*/
  opacity: 1;
  font-size: 2.5em;
}

/*Funcionamento*/
.header-leave-active,
.header-enter-active{
  /*transition: opacity 2s;*/
  transition: all 0.5s;
}

</style>
