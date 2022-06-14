<template>
  <div class="app">
    <div class="container">
      <div class="row">
        <!--div class="col-12 row">
          <div class="col-3" style="border: 1px solid black">
            <h1> {{ $store.state.display }} </h1>
          </div>
        <div class="col-3 nt-3">
          <input type="text" class="form-control" v-model="display">
        </div>
          <button class="btn btn-primary" @click="alteraDisplay">Alterando display</button>
        </div-->

        <div class="col-4">
          <h4> {{ $store.state.seconds }} </h4>
        </div>
        <div class="col-12">
          <button @click="inicializar">Iniciar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>


export default {
  name: 'App',
  data(){
    return{
      display: ''
      }
  },
  methods: {
    alteraDisplay(){
      //this.$store.state.display = this.display
      this.$store.commit('updateDisplay', this.display)
    },
    inicializar(){
      this.$store.dispatch('startCron')
    }
  }
}
</script>

<style>

</style>
