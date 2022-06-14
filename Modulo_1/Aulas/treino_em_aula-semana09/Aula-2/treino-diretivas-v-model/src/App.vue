<template>
  <div id="app">
    <p v-text="msg"></p>
    <p>v-model</p>
    <input type="text" v-model="msg">
    <br>
    <p>v-bind</p>
    <input type="text" :value="msg">
    <br>
    <p>v-model.lazy</p>
    <input type="text" v-model.lazy="msg">
    <br>
    <p>v-model.number:string</p>
    <label for="">{{ typeof msg }}</label>
    <input type="text" v-model.number="msg">
    <button @click="converte">Converter</button>
    <br>
    <p>v-model.trim</p>
    <input type="text" v-model.trim="msg">
  </div>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      colorLabel: '',
      msg: 'Bem vindo!',
      html: "<input type='number' class='colorRed' />"
    }
  },
  methods: {
    trocarMensagem(){
      this.msg = 'outra mesangem'
    },
    converte(){
      console.log(Number(this.msg))
    }
  }
}
</script>

<style>
.colorRed{
  color: red;
}
</style>