<template>
  <div id="app">
    <div>
      <div>
        <h1 v-demo>Configuração</h1>
      </div>
      <ul>
        <li v-for="item in lista" :key="item">
          {{ item }}
        </li>
      </ul>
    </div>
    <div>
      <ul>
        <li v-for="(item, index) in lista" :key="index">
          {{ index + '-' + item }}
        </li>
      </ul>
    </div>
    <div>
      <table>
        <tr>
          <th>Id</th>
          <th>Nome</th>
          <th>Idade</th>
        </tr>
        <tr v-for="(p, index) in pessoa" :key="index"> 
          <td>{{ index + 1}}</td>
          <td>{{ p.nome }}</td>
          <td>{{ p.idade }}</td>
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

</style>
