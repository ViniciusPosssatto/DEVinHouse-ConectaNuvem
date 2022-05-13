<template>
  <div class="app container">
    <span v-show="error" class="badge bg-danger">
      ID inválida! Tente novamente...
    </span>
    <div class="row">
      <div class="col-3">
          <label for="id">Digite uma ID:</label>
          <input type="number" id="id" class="form-control" v-model="id">
      </div>
      <div class="col-12 mt-2">
          <button @click="getUser" class="btn btn-primary">Buscar</button>
      </div>
      <div class="col-6">
        <span v-if="erro === false">Resultado: {{ user }}.</span>
        <span v-else>Usuário não encontrado.</span>
      </div>
    </div>
    <hr>
    <div class="col-12 mt-2">
          <button @click="getUsers" class="btn btn-primary">Buscar lista</button>
    </div>
    <div class="col-7" >
      <table class="table" v-if="users.length > 0">
        <thead>
          <tr>
            <th>Id</th>
            <th>Nome</th>
            <th>Data</th>
            <th>CEP</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="us in users" :key="us">
            <td>{{ us.id }}</td>
            <td>{{ us.nome }}</td>
            <td>{{ us.data }}</td>
            <td>{{ us.cep }}</td>
          </tr>
        </tbody>
      </table>
      <span v-else>Nenhum item na lista.</span>
    </div>
    <hr>
    <h4 style="color:blue">
      Formulário de cadastro de user:
    </h4>
    <div class="form">
      <form >
        <div class="row">
          <div class="col-3">
            <label for="nome">Nome</label>
            <input class="ms-2" type="text" v-model="user.nome">
          </div>
          <div class="col-3">
            <label for="data">Data</label>
            <input class="ms-2" type="date" v-model="user.data">
          </div>
          <div class="col-3">
            <label for="cep">CEP</label>
            <input class="ms-2" type="number" v-model="user.cep">
          </div>
          <div class="col-3">
            <button class="btn-secondary" @click.prevent="setUser">Enviar</button>
          </div>
        </div>
      </form>
    </div>
    <hr>
    <button class="btn-primary mt-2" @click="putUser">Atualizar</button>
    <button class="btn-danger ms-3" @click="deleteUser">Deletar</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
    data(){
      return {
        id: '',
        users: [],
        user: {},
        erro: false,
        error: false
      }
    },
    methods: {
      getUser() {
        axios.get(`https://6279994273bad506857ad40c.mockapi.io/api/v1/users/${this.id}`)
          .then((response) => {
            this.user = response.data;
          }) .catch((err) => {
            if(err){
              this.erro = true;
            }            
          })
          this.id = ''
      },
      getUsers(){
        axios.get(`https://6279994273bad506857ad40c.mockapi.io/api/v1/users`)
          .then((response) => {
            console.log(response.data)
            this.users = response.data;
          }) .catch((err) => {
            if(err){
              this.erro = true;
            }            
          })
      },
      setUser(){
        let user = this.user;
        axios.post('https://6279994273bad506857ad40c.mockapi.io/api/v1/users', {
          nome: user.nome,
          data: user.data,
          cep: user.cep
        }) .then((response) => {
          console.log(response)
        }) .catch((err) => {
          console.log(err.message)
        })
      },
      putUser(){
        //let user = this.user;
        axios.put(`https://6279994273bad506857ad40c.mockapi.io/api/v1/users/${this.id}`, {
          nome: this.user.nome,
          data: this.user.data,
          cep: this.user.cep
        }) .then((response) => {
          console.log(response.data)
        }) .catch(() => {
          this.error = true;
        })
      },
      deleteUser(){
        axios.delete(`https://6279994273bad506857ad40c.mockapi.io/api/v1/users/${this.id}`)
        .then((response) => {
          console.log(response)
        })
        .catch(() => {
          this.error = true;
        })
      }
    }
}
</script>

<style>
body{
  margin-top: 50px;
}
</style>
