<template>
<div>
  <div>
    <label for="">Digite algo para entrar na lista:</label>
    <input type="text" class="captura" v-model="item" id="captura-item">
  </div>
  <div>
    <table>
      
    </table>
  </div>
</div>
</template>

<script>


export default {
  name: 'App',
  components: {
   
  }
}


</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
table{
  border: 1px solid black;
}
</style>
