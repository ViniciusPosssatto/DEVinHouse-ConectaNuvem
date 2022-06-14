<template>
  <div class="app container">
    <div v-if="showw === false">
      <transition name="header" mode="in-out">
        <h1 v-if="show">Header!</h1>
        <span v-else>Header não disponível!</span>
      </transition>
    </div>
     
    <button @click="show = !show">Alterar Campo</button>
  </div>
</template>

<script>


export default {
  name: 'App',
  data(){
    return{
      show: true,
      showw: false
    }
  },
}
</script>

<style>

/*Primeiro estilo*/
.header-leave-to,
.header-enter-from{
  opacity: 0;
  font-size: 0px
}

/*Segundo estilo*/
.header-leave-from,
.header-enter-to{
  opacity: 1;
  font-size: 2.5em;
}

/*Funcionamento*/
.header-leave-active,
.header-enter-active{
  transition: all 0.5s;
}
.container{
  margin-top: 20px;
}

/*Primeiro estilo*/
.header-2-leave-to,
.header-2-enter-from{
  opacity: 0;
  font-size: 0px
}

/*Segundo estilo*/
.header-2-leave-from,
.header-2-enter-to{
  opacity: 1;
  font-size: 2.5em;
}

/*Funcionamento*/
.header-2-leave-active,
.header-2-enter-active{
  transition: all 0.5s;
}
</style>
