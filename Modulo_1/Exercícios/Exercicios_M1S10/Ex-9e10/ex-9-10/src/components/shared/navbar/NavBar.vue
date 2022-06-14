<template>
  <div>
      <nav class="navbar navbar-dark bg-dark"> 
        <router-link to="/home">Home</router-link>
        <router-link to="/pessoas/cadastro">Cadastro</router-link>
        <router-link to="/pessoas/listagem">Listagem</router-link>
        <div v-if="autenticado">
          <a href="#" @click="logout">Logout</a>
        </div>
        <div v-else>
          <router-link to="/login">Login</router-link>
        </div>
      </nav>

  </div>
</template>

<script>
//import RouterLink  from 'vue-router'
export default {  
  methods: {
        logout(){
            this.$store.commit('autenticacaoModule/logout');
        }
    },
    computed: {
        autenticado(){
            return this.$store.state.autenticacaoModule.autenticado; 
        }
    },
    mounted() {
        this.$store.state.autenticacaoModule.autenticado = localStorage.getItem('autenticado');
    }
}
</script>

<style>
.navbar{
  padding: 10px 20px;
}
</style>
