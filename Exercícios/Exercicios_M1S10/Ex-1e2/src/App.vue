<template>
  <div class="app container">
    <transition name="header" mode="in-out">
        <h1 v-show="show">Header!</h1>
    </transition>
     
    <button @click="show = !show">Alterar Campo</button>
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
</style>
