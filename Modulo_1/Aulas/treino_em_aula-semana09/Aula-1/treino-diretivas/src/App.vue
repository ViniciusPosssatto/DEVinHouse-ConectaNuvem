<template>
  <div id="app">

    <h1 v-text="msg" :style="'color: ' + colorLabel"></h1>
    <button @click="colorLabel = 'colorRed'">troca cor</button>
    <h1 @click="msg = 'nova Mensagem'" v-text="msg"></h1>

    <button @click="msg = 'nova Mensagem'">Trocar de Mensagem</button>
    <input type="color" v-model="coloLabel">
    <p v-html = "html"></p>
    
    {{ html }}
    <hr/>
    {{ trocarMensagem }}
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
    }
  }
}
</script>

<style>
.colorRed{
  color: red;
}
</style>