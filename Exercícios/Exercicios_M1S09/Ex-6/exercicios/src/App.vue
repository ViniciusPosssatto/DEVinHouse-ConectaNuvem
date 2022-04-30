<template>
  <div id="app">
    <div class="container">
      <ul class="list-group">
        <li v-for="item in lista" :key="item" class="list-group-item">
          {{ item }}
        </li>
      </ul>
    </div>
    <hr>
    <div class="container">
      <ul class="list-group">
        <li v-for="(item, index) in lista" :key="index" class="list-group-item">
          {{ index + '-' + item }}
        </li>
      </ul>
    </div>
    <hr>
    <div class="container">
      <table class="table">
        <tr>
          <th scope="col">Id</th>
          <th scope="col">Nome</th>
          <th scope="col">Idade</th>
        </tr>
        <tr v-for="(p, index) in pessoa" :key="index"> 
          <td scope="row">{{ index + 1}}</td>
          <td scope="row">{{ p.nome }}</td>
          <td scope="row">{{ p.idade }}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: "app",
  data() {
      return {
          lista: ['Item1', 'item2', 'inttem3'],
          pessoa: [{
            nome: 'Joao',
            idade: 50
            },{
              nome: 'Marcos',
            idade: 45
            },{
              nome: 'Lucas',
            idade: 44
          }]
      };
    },
}
</script>

<style>
ul{
  width: 40% !important;
}
table{
  width: 40% !important;
  background-color: rgb(204, 200, 200) !important;
  text-align: center;
}
</style>
