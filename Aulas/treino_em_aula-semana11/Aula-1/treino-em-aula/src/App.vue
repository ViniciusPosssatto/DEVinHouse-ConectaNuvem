<template>
 <div class="app">
   <button @click="buscaUsers">Get</button>
   <button @click="buscaUser">Get/ID</button>
   <button @click="salvaUser">Post</button>
   <button @click="atualizaUser">Put</button>
   <button @click="excluiUser">Delete</button>
  <hr>

  {{ users }}

  <hr>

  {{ user }}

 </div>
</template>

<script>

import axios from 'axios'
export default {
  name: 'App',
  data(){
  return {
      id: 2,
      users: [],
      user: {}
    }
  },
  components: {
    
  },
  methods: {
    buscaUsers(){
      axios.get('https://6279994273bad506857ad40c.mockapi.io/api/v1/users')
        .then((response) => {
          this.users = response.data
        }) .catch ((error) => {
          console.log(error.message)
        })
    
    },
    async buscaUser(){
      const promise = axios.get(`https://6279994273bad506857ad40c.mockapi.io/api/v1/users/${this.id}`)
      await promise.then((response) => {
        this.user = response.data;
      }) .catch((err) => { 
      console.log(err.message)
      })
    },
    salvaUser(){
    axios.post('https://6279994273bad506857ad40c.mockapi.io/api/v1/users', {
      name: 'novo usuário',
      email: 'novo@email.com'
      }).then((response) => {
        console.log(response.data)
      })
    },
    atualizaUser(){
    axios.put(`https://6279994273bad506857ad40c.mockapi.io/api/v1/users/${this.id}`, {
      name: 'novo nome!!'
      }).then((response) => {
        console.log(response.data)
      })
    },
    excluiUser(){
      axios.delete(`https://6279994273bad506857ad40c.mockapi.io/api/v1/users/${this.id}`)
      .then((response) => {
        console.log(response)
      }).catch((err) => {
        console.log(err.message)
      })
    }
  }
}
</script>

<style>

</style>
